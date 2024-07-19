import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QListWidgetItem, QFileDialog, QDialog, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QTime, QTimer, QElapsedTimer, pyqtSignal, QObject, QThread, QMetaObject, Q_ARG
from PyQt5 import QtCore
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import requests
from bs4 import BeautifulSoup
import re
import threading
import pyperclip  # Clipboard handling
import subprocess
import time

# Import the generated UI files
from ui_Splash import Ui_SplashScreen
from ui_MainWindow import Ui_MainWindow
from ui_Settings import Ui_Settings

# File to store settings
SETTINGS_FILE = 'settings.json'
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 750

# Start the URL capture script
subprocess.Popen(["python", "capture_url.py"])

# Load settings from file
def load_settings():
    try:
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
            for session in settings.get('sessions', []):
                if isinstance(session["start_time"], str):
                    session["start_time"] = QTime.fromString(session["start_time"], "HH:mm")
                if isinstance(session["end_time"], str):
                    session["end_time"] = QTime.fromString(session["end_time"], "HH:mm")
            return settings
    except FileNotFoundError:
        return {
            "wait_time": "5",
            "sessions": [],
            "categories": {},
            "whitelisted_sites": [],
            "blacklisted_sites": [],
            "productive_sites": [],  # Initialize productive_sites
            "override_delay": False,
            "warning_message": "Unproductive activity detected! For your own good, please return to being productive!"
        }

# Save settings to file
def save_settings(settings):
    settings_copy = {
        "wait_time": settings["wait_time"],
        "sessions": [
            {
                "start_time": session["start_time"].toString("HH:mm"),
                "end_time": session["end_time"].toString("HH:mm"),
                "days": session["days"]
            }
            for session in settings["sessions"]
        ],
        "categories": settings["categories"],
        "whitelisted_sites": settings["whitelisted_sites"],
        "blacklisted_sites": settings["blacklisted_sites"],
        "productive_sites": settings.get("productive_sites", []),  # Save productive_sites
        "override_delay": settings.get("override_delay", False),
        "warning_message": settings.get("warning_message", "Unproductive activity detected! For your own good, please return to being productive!")
    }
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings_copy, f, indent=4)

class Worker(QObject):
    url_captured = pyqtSignal(str)

    def run(self):
        previous_url = ""
        while True:
            current_url = pyperclip.paste()  # Read from clipboard
            print(f"Clipboard content: {current_url}")  # Debug logging
            if current_url and (current_url.startswith("http://") or current_url.startswith("https://")) and current_url != previous_url:
                previous_url = current_url
                self.url_captured.emit(current_url)
            else:
                print(f"Clipboard URL unchanged: {current_url}")
            time.sleep(2)  # Check every 2 seconds

# Splash Screen Class
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Define counter as an instance variable
        self.counter = 0

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(25)  # Timer in milliseconds

        self.show()

    def progress(self):
        self.ui.progressBar.setValue(self.counter)

        if self.counter > 200:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()

        self.counter += 1


# Main Window Class
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initialize the machine learning model
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.settings = load_settings()
        self.wait_time = int(self.settings.get("wait_time", "5"))
        self.sessions = self.settings.get("sessions", [])
        self.categories = self.settings.get("categories", {})
        self.whitelisted_sites = self.settings.get("whitelisted_sites", [])
        self.blacklisted_sites = self.settings.get("blacklisted_sites", [])
        self.productive_sites = self.settings.get("productive_sites", [])  # Load productive_sites
        self.override_delay = self.settings.get("override_delay", False)
        self.warning_message = self.settings.get("warning_message", "Unproductive activity detected! For your own good, please return to being productive!")

        self.unproductive_flag = False
        self.unproductive_timer = QElapsedTimer()
        self.warning_displayed = False  # Flag to indicate if a warning is displayed

        self.AddWhitelist.clicked.connect(self.add_to_whitelist)
        self.BrowseFile.clicked.connect(self.browse_file)
        self.RemoveWhitelist.clicked.connect(self.remove_selected_from_whitelist)
        self.AddBlacklist.clicked.connect(self.add_to_blacklist)
        self.BrowseFile_2.clicked.connect(self.browse_file_blacklist)
        self.RemoveBlacklist.clicked.connect(self.remove_selected_from_blacklist)
        self.Settings.clicked.connect(self.open_settings)

        self.category_sites = {
            "Social Media": ["facebook.com", "twitter.com", "instagram.com", "github.com"],
            "Games": ["crazygames.com", "store.epicgames.com", "store.steampowered.com"],
            "Video Entertainment": ["youtube.com", "netflix.com", "primevideo.com"],
            "Visual Entertainment": ["globalcomix.com", "mangadex.org", "manganato.com", "anime-planet.com", "readallcomics.com"],
            "Forums": ["reddit.com", "quora.com"],
            "Online Shopping": ["amazon.com", "alibaba.com", "aliexpress.com"],
            "Productivity Killers": ["nytimes.com/games/wordle", "nytimes.com/puzzles/spelling-bee", "nytimes.com/crosswords/game/mini"]
        }

        self.populate_unproductive_categories()
        self.populate_whitelisted_sites()
        self.populate_blacklisted_sites()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_sessions)
        self.timer.start(30000)  # Check every 30 seconds

        # Train the model
        self.train_model()

        # Monitor activity every 20 seconds
        self.activity_timer = QTimer()
        self.activity_timer.timeout.connect(self.monitor_activity)
        self.activity_timer.start(20000)

        # Setup worker thread
        self.worker = Worker()
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        
        self.worker.url_captured.connect(self.handle_captured_url)
        self.worker_thread.started.connect(self.worker.run)
        self.worker_thread.start()

    def handle_captured_url(self, url):
        print(f"Handling captured URL: {url}")
        current_website = url
        if current_website:
            if current_website in self.whitelisted_sites:
                self.unproductive_flag = False
                return
            if current_website in self.blacklisted_sites:
                self.unproductive_flag = True
            else:
                self.unproductive_flag = self.predict_unproductive(current_website)

            if self.unproductive_flag:
                if self.override_delay:
                    self.display_warning_message()
                else:
                    if not self.unproductive_timer.isValid():
                        self.unproductive_timer.start()
                    elif self.unproductive_timer.elapsed() >= self.wait_time * 60000:
                        self.display_warning_message()
                        self.unproductive_timer.invalidate()
            else:
                self.unproductive_flag = False
                self.unproductive_timer.invalidate()
        else:
            print("No current website detected.")

    def detect_unproductive_activity(self):
        current_website = self.get_current_website()
        if current_website:
            if current_website in self.whitelisted_sites:
                self.unproductive_flag = False
                self.unproductive_timer.invalidate()
                return
            if current_website in self.blacklisted_sites:
                self.unproductive_flag = True
            else:
                self.unproductive_flag = self.predict_unproductive(current_website)

            if self.unproductive_flag:
                if self.override_delay:
                    self.display_warning_message()
                else:
                    if not self.unproductive_timer.isValid():
                        self.unproductive_timer.start()
                    elif self.unproductive_timer.elapsed() >= self.wait_time * 60000:
                        self.display_warning_message()
                        self.unproductive_timer.invalidate()
            else:
                self.unproductive_flag = False
                self.unproductive_timer.invalidate()
        else:
            print("No current website detected.")

    def display_warning_message(self):
        if not self.warning_displayed:
            self.warning_displayed = True
            QMetaObject.invokeMethod(self, "show_warning_message", Qt.QueuedConnection)

    @QtCore.pyqtSlot()
    def show_warning_message(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Warning")
        dialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        dialog.showFullScreen()

        layout = QVBoxLayout(dialog)
        label = QLabel(self.warning_message, dialog)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: red;")
        layout.addWidget(label)

        close_button = QPushButton("Close", dialog)
        close_button.setStyleSheet("font-size: 18px; padding: 10px;")
        close_button.clicked.connect(dialog.accept)
        layout.addWidget(close_button)

        dialog.finished.connect(self.on_warning_closed)
        dialog.exec_()  # This makes the dialog modal

    @QtCore.pyqtSlot()
    def on_warning_closed(self):
        self.warning_displayed = False

    def populate_unproductive_categories(self):
        for category, examples in self.category_sites.items():
            checkbox = QCheckBox(category)
            checkbox.setStyleSheet("""
                QCheckBox {
                    font-family: 'Segoe UI';
                    font-size: 13pt;
                    color: #DC5F00;
                    background: transparent;
                }
            """)
            tooltip_text = "Examples: " + ", ".join(examples)
            checkbox.setToolTip(tooltip_text)
            self.Categories.addWidget(checkbox)
            checkbox.stateChanged.connect(lambda state, name=category: self.update_category_state(name, state))

            if category in self.categories:
                checkbox.setChecked(self.categories[category])

    def update_category_state(self, category_name, state):
        self.categories[category_name] = bool(state)
        self.settings["categories"] = self.categories
        save_settings(self.settings)
        self.train_model()  # Retrain the model when categories change

    def populate_whitelisted_sites(self):
        for site in self.whitelisted_sites:
            item = QListWidgetItem(site)
            self.Whitelist.addItem(item)

    def add_to_whitelist(self):
        url = self.EditWhitelist.text()
        if url:
            item = QListWidgetItem(url)
            self.Whitelist.addItem(item)
            self.whitelisted_sites.append(url)
            self.settings["whitelisted_sites"] = self.whitelisted_sites
            save_settings(self.settings)
            self.EditWhitelist.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a website or file address to whitelist.")

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Whitelist")
        if file_path:
            self.EditWhitelist.setText(file_path)

    def remove_selected_from_whitelist(self):
        selected_items = self.Whitelist.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "Please select an item to remove.")
            return
        for item in selected_items:
            self.whitelisted_sites.remove(item.text())
            self.settings["whitelisted_sites"] = self.whitelisted_sites
            save_settings(self.settings)
            self.Whitelist.takeItem(self.Whitelist.row(item))

    def populate_blacklisted_sites(self):
        for site in self.blacklisted_sites:
            item = QListWidgetItem(site)
            self.Blacklist.addItem(item)

    def add_to_blacklist(self):
        url = self.EditBlacklist.text()
        if url:
            item = QListWidgetItem(url)
            self.Blacklist.addItem(item)
            self.blacklisted_sites.append(url)
            self.settings["blacklisted_sites"] = self.blacklisted_sites
            save_settings(self.settings)
            self.EditBlacklist.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a website or file address to blacklist.")

    def browse_file_blacklist(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Blacklist")
        if file_path:
            self.EditBlacklist.setText(file_path)

    def remove_selected_from_blacklist(self):
        selected_items = self.Blacklist.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "Please select an item to remove.")
            return
        for item in selected_items:
            self.blacklisted_sites.remove(item.text())
            self.settings["blacklisted_sites"] = self.blacklisted_sites
            save_settings(self.settings)
            self.Blacklist.takeItem(self.Blacklist.row(item))

    def open_settings(self):
        self.settings_page = SettingsPage(self)
        self.settings_page.show()
        self.hide()

    def set_wait_time(self, wait_time):
        self.wait_time = int(wait_time)
        self.settings["wait_time"] = wait_time
        save_settings(self.settings)

    def get_wait_time(self):
        return self.wait_time

    def check_sessions(self):
        current_time = QTime.currentTime()
        current_day = QtCore.QDate.currentDate().dayOfWeek() - 1  # 0=Monday, 1=Tuesday, ..., 6=Sunday

        for session in self.sessions:
            if session["days"][current_day]:
                if session["start_time"] <= current_time <= session["end_time"]:
                    self.monitor_activity()
                    return  # Exit after finding the first active session

    def monitor_activity(self):
        threading.Thread(target=self.detect_unproductive_activity).start()

    def predict_unproductive(self, website):
        website_content = self.fetch_website_content(website)
        if not website_content:
            return False
        prediction = self.model.predict(self.vectorizer.transform([website_content]))
        return prediction[0] == "unproductive"

    def fetch_website_content(self, url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            return ' '.join(re.findall(r'\w+', soup.get_text().lower()))
        except Exception as e:
            print(f"Error fetching website content: {e}")
            return None

    def train_model(self):
        data = []
        labels = []
        # Add unproductive sites from category_sites
        for category, examples in self.category_sites.items():
            if self.categories.get(category):
                for site in examples:
                    content = self.fetch_website_content("http://" + site)
                    if content:
                        data.append(content)
                        labels.append("unproductive")
        # Add whitelisted sites as productive
        for site in self.whitelisted_sites:
            content = self.fetch_website_content("http://" + site)
            if content:
                data.append(content)
                labels.append("productive")
        # Add manually specified productive sites
        for site in self.productive_sites:
            content = self.fetch_website_content("http://" + site)
            if content:
                data.append(content)
                labels.append("productive")
        self.vectorizer.fit(data)
        self.model.fit(self.vectorizer.transform(data), labels)

    def get_current_website(self):
        current_url = pyperclip.paste()  # Read from clipboard
        print(f"Clipboard content: {current_url}")  # Debug logging
        if current_url and (current_url.startswith("http://") or current_url.startswith("https://")):
            return current_url
        else:
            print("Clipboard does not contain a valid URL")
            return None

    def send_warning_message(self):
        self.warning_displayed = True
        QMetaObject.invokeMethod(self, "show_warning_message", Qt.QueuedConnection)
        
        
# Settings Page Class
class SettingsPage(QMainWindow, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.sessions = self.parent().sessions

        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.ui.AddTiming.clicked.connect(self.add_session)
        self.ui.RemoveTiming.clicked.connect(self.remove_session)
        self.ui.Save.clicked.connect(self.save_settings)
        self.ui.BackHome.clicked.connect(self.go_back)  # Connect the back button

        self.OverrideDelay = self.ui.OverrideDelay
        self.WarningMessage = self.ui.Warning  # Ensure this matches the widget name in your UI file

        self.OverrideDelay.setChecked(self.parent().override_delay)
        self.WarningMessage.setPlainText(self.parent().warning_message)

        self.OverrideDelay.stateChanged.connect(self.set_override_delay)

        self.ui.Delay.addItems(["5", "10", "15", "30"])
        self.reload_settings_page()  # Load initial settings

    def add_session(self):
        start_time = self.ui.Start.time()
        end_time = self.ui.End.time()
        days = [self.ui.monday.isChecked(), self.ui.tuesday.isChecked(), self.ui.wednesday.isChecked(),
                self.ui.thursday.isChecked(), self.ui.friday.isChecked(), self.ui.saturday.isChecked(),
                self.ui.sunday.isChecked()]

        session = {
            "start_time": start_time,
            "end_time": end_time,
            "days": days
        }

        self.sessions.append(session)
        self.update_sessions_list()

    def update_sessions_list(self):
        self.ui.ExistingRunTimes.clear()
        for session in self.sessions:
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            active_days = [days[i] for i, active in enumerate(session["days"]) if active]
            item_text = f"{session['start_time'].toString()} - {session['end_time'].toString()} : {', '.join(active_days)}"
            self.ui.ExistingRunTimes.addItem(item_text)

    def remove_session(self):
        selected_items = self.ui.ExistingRunTimes.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            index = self.ui.ExistingRunTimes.row(item)
            del self.sessions[index]
            self.ui.ExistingRunTimes.takeItem(index)

    def save_settings(self):
        wait_time = self.ui.Delay.currentText()
        self.parent().set_wait_time(wait_time)
        self.parent().sessions = self.sessions
        self.parent().settings["sessions"] = self.sessions
        self.parent().settings["override_delay"] = self.OverrideDelay.isChecked()
        self.parent().settings["warning_message"] = self.WarningMessage.toPlainText()
        save_settings(self.parent().settings)
        print("Settings saved")
        self.reload_settings_page()

    def set_override_delay(self, state):
        self.parent().override_delay = bool(state)
        self.parent().settings["override_delay"] = self.parent().override_delay
        save_settings(self.parent().settings)

    def reload_settings_page(self):
        self.parent().settings = load_settings()
        self.update_sessions_list()
        current_wait_time = self.parent().get_wait_time()
        index = self.ui.Delay.findText(str(current_wait_time))  # Ensure the argument is a string
        if index != -1:
            self.ui.Delay.setCurrentIndex(index)
        self.OverrideDelay.setChecked(self.parent().settings["override_delay"])
        self.WarningMessage.setPlainText(self.parent().settings["warning_message"])

    def showEvent(self, event):
        super().showEvent(event)
        self.reload_settings_page()

    def go_back(self):
        self.parent().override_delay = self.OverrideDelay.isChecked()
        self.parent().warning_message = self.WarningMessage.toPlainText()

        self.parent().show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
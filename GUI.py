import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QListWidgetItem, QFileDialog, QDialog, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QTime, QTimer, QElapsedTimer, pyqtSlot, QMetaObject
from PyQt5 import QtCore
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from PIL import ImageGrab, Image
import pytesseract
import threading
import requests
from bs4 import BeautifulSoup
import re
import os

from PyQt5.QtCore import QThread, pyqtSignal

#set up model trainer thread so UI can still be responsive while... training
class ModelTrainer(QThread):
    training_finished = pyqtSignal()

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        self.main_window.train_model()
        self.training_finished.emit()

# Import the UI files I generated using PyQt designer
from ui_Splash import Ui_SplashScreen
from ui_MainWindow import Ui_MainWindow
from ui_Settings import Ui_Settings

# Link to my file to save settings
SETTINGS_FILE = 'settings.json'
SCREEN_WIDTH = 1045 #Currently not in use, but ... 
SCREEN_HEIGHT = 600

# Load settings saved in settings file, at start of program
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
            "productive_sites": [],  #
            "override_delay": False,
            "warning_message": "Unproductive activity detected! For your own good, please return to being productive!"
        }

# Save new settings to settings.json
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

# My Splash Screen
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground) #Not too sure what this does, just saw it on a tutorial

        self.counter = 0

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(50)  # Timer in milliseconds

        self.show()

        # My main window instance
        self.main_window = MainWindow()

        # Start training the ML unproductive activity detection model
        self.model_trainer = ModelTrainer(self.main_window)
        self.model_trainer.training_finished.connect(self.on_training_finished)
        self.model_trainer.start()

    #Existing purely for visual reasons: to make the progress bar move
    def progress(self):
        self.ui.progressBar.setValue(self.counter)

        if self.counter > 100:
            self.timer.stop()
            self.main_window.show()
            self.close()

        self.counter += 1

    def on_training_finished(self):
        print("Model training completed.")
        self.main_window.on_training_finished()


# Have to set up path to tesseract... 
tesseract_path = os.path.join(os.path.dirname(__file__), 'Tesseract-OCR', 'tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path

#My mainwindow
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
         # Enable DPI scaling, apparently helps with scaling but clearly not
        app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

        self.currently_in_session = False
        self.model_trained = False

        # Initialize the ML model
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

        #Set up.. from previously saved settings
        self.settings = load_settings()
        self.wait_time = int(self.settings.get("wait_time", "5"))
        self.sessions = self.settings.get("sessions", [])
        self.categories = self.settings.get("categories", {})
        self.whitelisted_sites = self.settings.get("whitelisted_sites", [])
        self.blacklisted_sites = self.settings.get("blacklisted_sites", [])
        self.productive_sites = self.settings.get("productive_sites", [])
        self.override_delay = self.settings.get("override_delay", False)
        self.warning_message = self.settings.get("warning_message", "Unproductive activity detected! For your own good, please return to being productive!")

        self.unproductive_flag = False
        self.unproductive_timer = QElapsedTimer()
        self.warning_displayed = False

        self.AddWhitelist.clicked.connect(self.add_to_whitelist)
        self.BrowseFile.clicked.connect(self.browse_file)
        self.RemoveWhitelist.clicked.connect(self.remove_selected_from_whitelist)
        self.AddBlacklist.clicked.connect(self.add_to_blacklist)
        self.BrowseFile_2.clicked.connect(self.browse_file_blacklist)
        self.RemoveBlacklist.clicked.connect(self.remove_selected_from_blacklist)
        self.Settings.clicked.connect(self.open_settings)

        #Unproductive category names w example site links
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

        self.session_check_timer = QTimer()
        self.session_check_timer.timeout.connect(self.check_sessions)
        self.session_check_timer.start(10000)  # Check every 10 seconds for whether current time is within an existing session time

        self.activity_monitor_timer = QTimer()
        self.activity_monitor_timer.timeout.connect(self.detect_unproductive_activity)
        self.activity_monitor_timer.start(15000)  # Check every 15 seconds for screen activity

    def on_training_finished(self):
        self.model_trained = True
        print("Model training completed.")

    def capture_screen(self):
        screen = ImageGrab.grab()
        return screen

    def extract_text_from_image(self, image):
        try:
            text = pytesseract.image_to_string(image)
            return text
        except pytesseract.TesseractNotFoundError:
            print("Tesseract is not found in the path used")
            return ""
        except Exception as e:
            print(f"{e}")
            return ""

    def detect_unproductive_activity(self):
        if not self.currently_in_session:
            print("Current time is not within any session. Will not proceed with activity detection.")
            return

        if not self.model_trained:
            print("Model is not yet trained. Will not proceed with activity detection.")
            return

        print("Detecting unproductive activity...")
        screen_image = self.capture_screen()
        screen_text = self.extract_text_from_image(screen_image)

        if screen_text.strip():
            print("Extracted text from screen:", screen_text)
            self.unproductive_flag = self.predict_unproductive(screen_text)
            print(f"Screen text is {'unproductive' if self.unproductive_flag else 'productive'}.")

            if self.unproductive_flag: # checks if the unproductive flag, which symbolises whether unproductive activity has been detected
                if self.override_delay:
                    print("Override delay is enabled, displaying warning message immediately.")
                    self.display_warning_message() #if the override delay button in settings window is clicked, a warning message is shown immediately upon unproductive activity detection
                else:
                    if not self.unproductive_timer.isValid():
                        print("Starting unproductive timer.")
                        self.unproductive_timer.start()
                    elif self.unproductive_timer.elapsed() >= self.wait_time * 60000:
                        print(f"Unproductive timer elapsed {self.wait_time} minutes, displaying warning message.")
                        self.display_warning_message()
                        self.unproductive_timer.invalidate()
                    else:
                        remaining_time = self.wait_time * 60000 - self.unproductive_timer.elapsed()
                        print(f"Unproductive timer running. Time remaining: {remaining_time // 60000} minutes and {remaining_time % 60000 // 1000} seconds.")
            else:
                print("Resetting unproductive flag and timer.")
                self.unproductive_flag = False
                self.unproductive_timer.invalidate()
        else:
            print("No text detected on screen.")

    @QtCore.pyqtSlot()
    def show_warning_message(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Warning")
        dialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint) #So it shows up and pops up
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
        self.unproductive_flag = False
        self.unproductive_timer.invalidate()
        print("Warning message closed. Resetting state.")

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
        if self.model_trained:
            self.start_training()  # Retrain the model when chosen unproductive categories change

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
            QMessageBox.warning(self, "Input Error", "Please enter a website to whitelist.")

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Whitelist")
        if file_path:
            self.EditWhitelist.setText(file_path)

    def remove_selected_from_whitelist(self):
        selected_items = self.Whitelist.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "Please select a link to remove.")
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
            QMessageBox.warning(self, "Input Error", "Please enter a website to blacklist.")

    def browse_file_blacklist(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Blacklist")
        if file_path:
            self.EditBlacklist.setText(file_path)

    def remove_selected_from_blacklist(self):
        selected_items = self.Blacklist.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "Please select a link to remove.")
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
        current_day = QtCore.QDate.currentDate().dayOfWeek() - 1  # Note to self: 0=Monday, 1=Tuesday ... 6=Sunday

        in_session = False
        for session in self.sessions:
            start_time = session["start_time"]
            end_time = session["end_time"]

            if session["days"][current_day]:
                if end_time < start_time:  # For if end time is past midnight
                    if current_time >= start_time or current_time <= end_time:
                        in_session = True
                        print(f"Current time {current_time.toString()} is within session: {start_time.toString()} - {end_time.toString()} (spans midnight)")
                        break
                else:
                    if start_time <= current_time <= end_time: #
                        in_session = True
                        print(f"Current time {current_time.toString()} is within session: {start_time.toString()} - {end_time.toString()}")
                        break

        if in_session and not self.currently_in_session:
            print(f"Current time {current_time.toString()} is within a session.")
            self.currently_in_session = True
        elif not in_session and self.currently_in_session:
            print(f"Current time {current_time.toString()} is not within any session.")
            self.currently_in_session = False

    def monitor_activity(self):
        self.activity_monitor_timer.start() #start of checking whether screen activity is unproductive..

    def predict_unproductive(self, text):
        if not self.currently_in_session or not self.model_trained:
            return False

        content_features = self.vectorizer.transform([text])
        prediction = self.model.predict(content_features)
        return prediction[0] == "unproductive"
    
    def start_training(self):
            if self.model_trainer.isRunning():
                self.model_trainer.terminate()

            self.model_trainer = ModelTrainer(self)
            self.model_trainer.training_finished.connect(self.on_training_finished)
            self.model_trainer.start()
            
    def train_model(self):
        data = []
        labels = []

        # Use the example sites listed from chosen unproductive categories to train
        for category, examples in self.category_sites.items():
            if self.categories.get(category):
                for site in examples:
                    content = self.fetch_website_content("http://" + site)
                    if content:
                        data.append(content)
                        labels.append("unproductive")
            else:
                for site in examples:
                    content = self.fetch_website_content("http://" + site)
                    if content:
                        data.append(content)
                        labels.append("productive")

        # Train ML to detect content of whitelisted sites as productive
        for site in self.whitelisted_sites:
            content = self.fetch_website_content("http://" + site)
            if content:
                data.append(content)
                labels.append("productive")
                
        # Treat blacklisted sites as unproductive
        for site in self.blacklisted_sites:
            content = self.fetch_website_content("http://" + site)
            if content:
                data.append(content)
                labels.append("unproductive")

        # Add manually specified productive sites (from settings.json)
        for site in self.productive_sites:
            content = self.fetch_website_content("http://" + site)
            if content:
                data.append(content)
                labels.append("productive")

        self.vectorizer.fit(data)
        self.model.fit(self.vectorizer.transform(data), labels)

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

    def display_warning_message(self):
        self.warning_displayed = True
        QMetaObject.invokeMethod(self, "show_warning_message", Qt.QueuedConnection)

    def send_warning_message(self):
        if not self.warning_displayed:
            self.display_warning_message()
        
# Settings Page Class
class SettingsPage(QMainWindow, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.sessions = self.parent().sessions
         # Enable DPI scaling
        app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

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
        self.parent().settings = load_settings()  # Reload settings from file
        self.sessions = self.parent().settings.get("sessions", [])
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
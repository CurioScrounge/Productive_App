 
    
    
    
    
    
    
import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QListWidgetItem, QFileDialog, QMessageBox, QTextEdit
from PyQt5.QtCore import Qt, QTime, QTimer, QElapsedTimer
from PyQt5 import QtCore
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import requests
from bs4 import BeautifulSoup
import re
import threading

# Import the generated UI files
from ui_Splash import Ui_SplashScreen
from ui_MainWindow import Ui_MainWindow
from ui_Settings import Ui_Settings

# File to store settings
SETTINGS_FILE = 'settings.json'
ScreenWidth = 1100
ScreenHeight = 750

# Load settings from file
def load_settings():
    try:
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
            # Convert session times back to QTime objects
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
            "override_delay": False,
            "warning_message": "Unproductive activity detected! For your own good, please return to being productive!"
        }

# Save settings to file
def save_settings(settings):
    # Create a copy of the settings to convert QTime objects to strings
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
        "override_delay": settings.get("override_delay", False),
        "warning_message": settings.get("warning_message", "Unproductive activity detected! For your own good, please return to being productive!")
    }
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings_copy, f, indent=4)

# Global counter for the splash screen
counter = 0

# Splash Screen Class
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # Remove title bar and make the splash screen transparent
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Start the timer for the splash screen
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(25)  # Timer in milliseconds

        # Show the splash screen
        self.show()

    def progress(self):
        global counter

        # Set value to progress bar
        self.ui.progressBar.setValue(counter)

        # Close splash screen and open the main window
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()

        # Increase counter
        counter += 1

# Main Window Class
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set fixed size for the main window
        self.setFixedSize(ScreenWidth, ScreenHeight)

        # Load settings
        self.settings = load_settings()
        self.wait_time = self.settings.get("wait_time", "5")
        self.sessions = self.settings.get("sessions", [])
        self.categories = self.settings.get("categories", {})
        self.whitelisted_sites = self.settings.get("whitelisted_sites", [])
        self.blacklisted_sites = self.settings.get("blacklisted_sites", [])
        self.override_delay = self.settings.get("override_delay", False)
        self.warning_message = self.settings.get("warning_message", "Unproductive activity detected! For your own good, please return to being productive!")

        # Track unproductive activity
        self.unproductive_flag = False
        self.unproductive_timer = QElapsedTimer()

        # Connect signals to slots
        self.AddWhitelist.clicked.connect(self.add_to_whitelist)
        self.BrowseFile.clicked.connect(self.browse_file)
        self.RemoveWhitelist.clicked.connect(self.remove_selected_from_whitelist)
        self.AddBlacklist.clicked.connect(self.add_to_blacklist)
        self.BrowseFile_2.clicked.connect(self.browse_file_blacklist)
        self.RemoveBlacklist.clicked.connect(self.remove_selected_from_blacklist)
        self.Settings.clicked.connect(self.open_settings)

        # Example categories and sites
        self.category_sites = {
            "Social Media": ["facebook.com", "twitter.com", "instagram.com", "github.com"],
            "Games": ["crazygames.com", "store.epicgames.com", "store.steampowered.com"],
            "Video Entertainment": ["youtube.com", "netflix.com", "primevideo.com"],
            "Visual Entertainment": ["globalcomix.com", "mangadex.org", "manganato.com", "anime-planet.com", "readallcomics.com"],
            "Forums": ["reddit.com", "quora.com"],
            "Online Shopping": ["amazon.com", "alibaba.com", "aliexpress.com"],
            "Productivity Killers": ["nytimes.com/games/wordle", "nytimes.com/puzzles/spelling-bee", "nytimes.com/crosswords/game/mini"]
        }

        # Populate unproductive categories with customized checkboxes
        self.populate_unproductive_categories()

        # Populate whitelisted sites
        self.populate_whitelisted_sites()

        # Populate blacklisted sites
        self.populate_blacklisted_sites()

        # Timer to check the current time against sessions
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_sessions)
        self.timer.start(60000)  # Check every minute

        # Initialize the machine learning model
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

        # Train the model
        self.train_model()

        

    def populate_unproductive_categories(self):
        for category, examples in self.category_sites.items():
            checkbox = QCheckBox(category)
            # Customize the checkbox font and style
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

            # Set the checkbox state based on the saved settings
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
        self.wait_time = wait_time
        self.settings["wait_time"] = wait_time
        save_settings(self.settings)

    def get_wait_time(self):
        return self.wait_time

    def check_sessions(self):
        current_time = QTime.currentTime()
        current_day = QtCore.QDate.currentDate().dayOfWeek() - 1  # 0=Monday, 1=Tuesday, ..., 6=Sunday

        for session in self.sessions:
            if session["days"][current_day]:
                while session["start_time"] <= current_time <= session["end_time"]:
                    # Timer to check website activity
                    self.activity_timer = QTimer()
                    self.activity_timer.timeout.connect(self.monitor_activity)
                    self.activity_timer.start(30000)  # Check every 20 seconds

    def monitor_activity(self):
        threading.Thread(target=self.detect_unproductive_activity).start()

    def detect_unproductive_activity(self):
        # Logic to detect unproductive activity
        current_website = self.get_current_website()
        if current_website in self.whitelisted_sites:
            self.unproductive_flag = False
            return
        if current_website in self.blacklisted_sites:
            self.unproductive_flag = True
        else:
            self.unproductive_flag = self.predict_unproductive(current_website)

        if self.unproductive_flag:
            if self.override_delay:
                self.send_warning_message()
            else:
                if not self.unproductive_flag:
                    self.unproductive_flag = True
                    self.unproductive_timer.start()
                elif self.unproductive_timer.elapsed() >= int(self.wait_time) * 60000:
                    self.send_warning_message()
                    self.unproductive_flag = False
        else:
            self.unproductive_flag = False

    def predict_unproductive(self, website):
        # Predict if the website is unproductive using the trained model
        website_content = self.fetch_website_content(website)
        if not website_content:
            return False
        prediction = self.model.predict(self.vectorizer.transform([website_content]))
        return prediction[0] == "unproductive"

    def fetch_website_content(self, url):
        # Fetch the website content for classification
        try:
            response = requests.get("http://" + url)
            soup = BeautifulSoup(response.text, 'html.parser')
            return ' '.join(re.findall(r'\w+', soup.get_text().lower()))
        except Exception as e:
            print(f"Error fetching website content: {e}")
            return None

    def train_model(self):
        # Train the machine learning model based on user-selected categories
        data = []
        labels = []
        for category, examples in self.category_sites.items():
            if self.categories.get(category):
                for site in examples:
                    content = self.fetch_website_content(site)
                    if content:
                        data.append(content)
                        labels.append("unproductive")
        for site in self.whitelisted_sites:
            content = self.fetch_website_content(site)
            if content:
                data.append(content)
                labels.append("productive")
        self.vectorizer.fit(data)
        self.model.fit(self.vectorizer.transform(data), labels)

    def get_current_website(self):
        # Placeholder for getting the current website the user is visiting
        # This needs to be implemented using a browser extension or similar method
        return "example.com"

    def send_warning_message(self):
        QMessageBox.warning(self, "Warning", self.warning_message)

class SettingsPage(QMainWindow, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.sessions = self.parent().sessions

        # Set fixed size for the settings
        self.setFixedSize(ScreenWidth, ScreenHeight)

        # Connect buttons
        self.ui.AddTiming.clicked.connect(self.add_session)
        self.ui.RemoveTiming.clicked.connect(self.remove_session)
        self.ui.Save.clicked.connect(self.save_settings)
        self.ui.BackHome.clicked.connect(self.go_back)  # Connect the back button

        # Use existing widgets from the designer
        self.OverrideDelay = self.ui.OverrideDelay
        self.WarningMessage = self.ui.Warning  # Ensure this matches the widget name in your UI file

        # Set initial values for override delay and warning message
        self.OverrideDelay.setChecked(self.parent().override_delay)
        self.WarningMessage.setPlainText(self.parent().warning_message)

        self.OverrideDelay.stateChanged.connect(self.set_override_delay)

        # Add predefined wait times to the combo box
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
        # Save the settings, including the wait time
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
        # Reload settings from file to ensure the latest values are reflected
        self.parent().settings = load_settings()

        # Clear and reload the settings page
        self.update_sessions_list()
        # Set the delay period to the currently saved wait time
        current_wait_time = self.parent().get_wait_time()
        index = self.ui.Delay.findText(current_wait_time)
        if index != -1:
            self.ui.Delay.setCurrentIndex(index)
        # Set the override delay checkbox
        self.OverrideDelay.setChecked(self.parent().settings["override_delay"])
        # Set the warning message text
        self.WarningMessage.setPlainText(self.parent().settings["warning_message"])

    def showEvent(self, event):
        super().showEvent(event)
        # Reload the settings when the settings page is shown
        self.reload_settings_page()

    def go_back(self):
        # Update parent settings before going back
        self.parent().override_delay = self.OverrideDelay.isChecked()
        self.parent().warning_message = self.WarningMessage.toPlainText()

        self.parent().show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
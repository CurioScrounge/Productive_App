import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QCheckBox, QListWidget, QFileDialog, QMessageBox, QSizePolicy, QTimeEdit, QComboBox, QFormLayout, QListWidgetItem
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

# Import the generated UI files
from ui_Splash import Ui_SplashScreen
from ui_MainWindow import Ui_MainWindow
from ui_Settings import Ui_Settings

# File to store settings
SETTINGS_FILE = 'settings.json'

# Load settings from file
def load_settings():
    try:
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "wait_time": "5",
            "sessions": [],
            "categories": {},
            "whitelisted_sites": []
        }

# Save settings to file
def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)

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

        # Load settings
        self.settings = load_settings()
        self.wait_time = self.settings.get("wait_time", "5")
        self.sessions = self.settings.get("sessions", [])
        self.categories = self.settings.get("categories", {})
        self.whitelisted_sites = self.settings.get("whitelisted_sites", [])

        # Connect signals to slots
        self.AddWhitelist.clicked.connect(self.add_to_whitelist)
        self.BrowseFile.clicked.connect(self.browse_file)
        self.RemoveWhitelist.clicked.connect(self.remove_selected_from_whitelist)
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

        # Populate unproductive categories with checkboxes and tooltips
        self.populate_unproductive_categories()

        # Populate whitelisted sites
        self.populate_whitelisted_sites()

        # Timer to check the current time against sessions
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_sessions)
        self.timer.start(60000)  # Check every minute

        # Apply size policies and stretch factors
        self.apply_size_policies()

    def populate_unproductive_categories(self):
        for category, examples in self.category_sites.items():
            self.add_category(category, examples)

        for category_name, checked in self.categories.items():
            for _, checkbox, _ in self.categories:
                if checkbox.text() == category_name:
                    checkbox.setChecked(checked)

    def add_category(self, category_name, examples):
        checkbox = QCheckBox(category_name)
        tooltip_text = "Examples: " + ", ".join(examples)
        checkbox.setToolTip(tooltip_text)
        self.Categories.addWidget(checkbox)
        self.categories[category_name] = checkbox.isChecked()
        checkbox.stateChanged.connect(lambda state, name=category_name: self.update_category_state(name, state))

    def update_category_state(self, category_name, state):
        self.categories[category_name] = bool(state)
        self.settings["categories"] = self.categories
        save_settings(self.settings)

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

    def apply_size_policies(self):
        # Set size policies for dynamic resizing
        widgets = [self.EditWhitelist, self.AddWhitelist, self.BrowseFile, self.Whitelist, self.RemoveWhitelist]
        for widget in widgets:
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def resizeEvent(self, event):
        new_size = event.size()

        # Calculate the new font size based on the window size
        font_size = max(10, new_size.height() // 40)
        font = QFont()
        font.setPointSize(font_size)

        # Apply the new font to all widgets
        widgets = [self.EditWhitelist, self.AddWhitelist, self.BrowseFile, self.Whitelist, self.RemoveWhitelist]
        for category_name, checkbox, examples in self.categories.items():
            checkbox.setFont(font)
        for widget in widgets:
            widget.setFont(font)

        super().resizeEvent(event)

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
                if session["start_time"] <= current_time <= session["end_time"]:
                    self.run_program()

    def run_program(self):
        # Convert wait time to seconds
        wait_seconds = int(self.wait_time) * 60
        # Logic to run the program
        print(f"Program is running based on scheduled time with a wait time of {wait_seconds} seconds")

# Settings Page Class
class SettingsPage(QMainWindow, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.sessions = self.parent().sessions

        # Connect buttons
        self.AddTiming.clicked.connect(self.add_session)
        self.RemoveTiming.clicked.connect(self.remove_session)
        self.Save.clicked.connect(self.save_settings)
        self.BackHome.clicked.connect(self.go_back)  # Connect the back button

        # Add predefined wait times to the combo box
        self.Delay.addItems(["5", "10", "15", "30"])
        self.reload_settings_page()  # Load initial settings

    def add_session(self):
        start_time = self.Start.time()
        end_time = self.End.time()
        days = [self.monday.isChecked(), self.tuesday.isChecked(), self.wednesday.isChecked(),
                self.thursday.isChecked(), self.friday.isChecked(), self.saturday.isChecked(),
                self.sunday.isChecked()]

        session = {
            "start_time": start_time,
            "end_time": end_time,
            "days": days
        }

        self.sessions.append(session)
        self.update_sessions_list()

    def update_sessions_list(self):
        self.ExistingRunTimes.clear()
        for session in self.sessions:
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            active_days = [days[i] for i, active in enumerate(session["days"]) if active]
            item_text = f"{session['start_time'].toString()} - {session['end_time'].toString()} : {', '.join(active_days)}"
            self.ExistingRunTimes.addItem(item_text)

    def remove_session(self):
        selected_items = self.ExistingRunTimes.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            index = self.ExistingRunTimes.row(item)
            del self.sessions[index]
            self.ExistingRunTimes.takeItem(index)

    def save_settings(self):
        # Save the settings, including the wait time
        wait_time = self.Delay.currentText()
        self.parent().set_wait_time(wait_time)
        self.parent().sessions = self.sessions
        self.parent().settings["sessions"] = self.sessions
        save_settings(self.parent().settings)
        print("Settings saved")
        self.reload_settings_page()

    def reload_settings_page(self):
        # Clear and reload the settings page
        self.update_sessions_list()
        # Set the delay period to the currently saved wait time
        current_wait_time = self.parent().get_wait_time()
        index = self.Delay.findText(current_wait_time)
        if index != -1:
            self.Delay.setCurrentIndex(index)

    def go_back(self):
        self.parent().show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
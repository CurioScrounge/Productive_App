from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QCheckBox, QTimeEdit, QSpinBox, QListWidgetItem, QFileDialog, QMessageBox, QSizePolicy, QWidget
from PyQt5.QtCore import Qt, QSize

import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)

## ==> SPLASH SCREEN
from ui_Splash import Ui_SplashScreen
from ui_MainWindow import Ui_MainWindow

## ==> GLOBALS
counter = 0

# # YOUR APPLICATION
class UnproductiveSelections(QMainWindow):
     def __init__(self):
         QMainWindow.__init__(self)
         self.ui = Ui_MainWindow()
         self.ui.setupUi(self)


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(25)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            
            # STOP TIMER
            self.timer.stop()
            
            #Show main window
            self.main = MainWindow()
            self.main.show()
            
            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

#Main Window
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect signals to slots
        self.AddWhitelist.clicked.connect(self.add_to_whitelist)
        self.BrowseFile.clicked.connect(self.browse_file)
        self.RemoveWhitelist.clicked.connect(self.remove_selected_from_whitelist)  # Connect the remove button

        self.categories = []

        # Example categories and sites
        self.category_sites = {
            "Social Media": ["facebook.com", "twitter.com", "instagram.com", "github.com"],
            "Games": ["crazygames.com", "store.epicgames.com", "store.steampowered.com"],
            "Video Entertainment": ["youtube.com", "netflix.com", "primevideo.com"],
            "Visual Entertainment": ["globalcomix.com","mangadex.org","manganato.com","anime-planet.com", "readallcomics.com"],
            "Forums": ["reddit.com","quora.com"],
            "Online Shopping": ["amazon.com", "alibaba.com", "aliexpress.com", ],
            "Productivity Killers": ["nytimes.com/games/wordle","nytimes.com/puzzles/spelling-bee","nytimes.com/crosswords/game/mini"]
        }

        # Populate unproductive categories with checkboxes and tooltips
        self.populate_unproductive_categories()

    # Apply size policies and stretch factors
        self.apply_size_policies()
        
    def populate_unproductive_categories(self):
        for category, examples in self.category_sites.items():
            self.add_category(category, examples)

    def add_category(self, category_name, examples):
        checkbox = QCheckBox(category_name)
        tooltip_text = "Examples: " + ", ".join(examples)
        checkbox.setToolTip(tooltip_text)
        self.Categories.addWidget(checkbox)
        self.categories.append((category_name, checkbox, examples))

    def add_to_whitelist(self):
        url = self.EditWhitelist.text()
        if url:
            item = QListWidgetItem(url)
            self.Whitelist.addItem(item)
            self.EditWhitelist.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a website or file address to whitelist.")

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Whitelist")
        if file_path:
            self.EditWhitelist.setText(file_path)

    def apply_size_policies(self):
        # Set size policies for dynamic resizing
        widgets = [self.EditWhitelist, self.AddWhitelist, self.BrowseFile, self.Whitelist, self.RemoveWhitelist]
        for widget in widgets:
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def remove_selected_from_whitelist(self):
        selected_items = self.Whitelist.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "Please select an item to remove.")
            return
        for item in selected_items:
            self.Whitelist.takeItem(self.Whitelist.row(item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QCheckBox, QTimeEdit, QSpinBox

import sys

def window():
    app = QApplication(sys.argv) #get system being worked on
    win=QMainWindow()  #set up window for UI
    win.setGeometry(100,200,800,600) #Where the window should show up and dimensions
    win.setWindowTitle("Configure settings")    #Title of window
    
    win.show() #To show window
    sys.exit(app.exec_())  #To ensure when we exit, the application closes properly

window() #call function to show window
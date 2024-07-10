# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowqnVSHx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(974, 677)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(55, 58, 64);\n"
"}\n"
"\n"
"QCheckBox{\n"
"	font: 75 12pt \"Segoe UI\";\n"
"	color: rgb(104, 109, 118);\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 301, 621))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 80, 281, 541))
        self.Categories = QVBoxLayout(self.verticalLayoutWidget)
        self.Categories.setObjectName(u"Categories")
        self.Categories.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 281, 41))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(310, 20, 661, 621))
        self.EditWhitelist = QLineEdit(self.groupBox_2)
        self.EditWhitelist.setObjectName(u"EditWhitelist")
        self.EditWhitelist.setGeometry(QRect(60, 80, 481, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.EditWhitelist.setFont(font1)
        self.EditWhitelist.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.BrowseFile = QPushButton(self.groupBox_2)
        self.BrowseFile.setObjectName(u"BrowseFile")
        self.BrowseFile.setGeometry(QRect(10, 80, 41, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        self.BrowseFile.setFont(font2)
        self.BrowseFile.setLayoutDirection(Qt.LeftToRight)
        self.BrowseFile.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(104, 109, 118);\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.BrowseFile.setCheckable(False)
        self.AddWhitelist = QPushButton(self.groupBox_2)
        self.AddWhitelist.setObjectName(u"AddWhitelist")
        self.AddWhitelist.setGeometry(QRect(550, 80, 61, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.AddWhitelist.setFont(font3)
        self.AddWhitelist.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(55, 58, 64);\n"
"}")
        self.AddWhitelist.setCheckable(False)
        self.AddWhitelist.setFlat(False)
        self.Whitelist = QListWidget(self.groupBox_2)
        self.Whitelist.setObjectName(u"Whitelist")
        self.Whitelist.setGeometry(QRect(10, 130, 601, 481))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setItalic(False)
        self.Whitelist.setFont(font4)
        self.Whitelist.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(55, 58, 64);\n"
"}")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 30, 361, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.RemoveWhitelist = QPushButton(self.groupBox_2)
        self.RemoveWhitelist.setObjectName(u"RemoveWhitelist")
        self.RemoveWhitelist.setGeometry(QRect(620, 140, 31, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveWhitelist.sizePolicy().hasHeightForWidth())
        self.RemoveWhitelist.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setWeight(75)
        self.RemoveWhitelist.setFont(font5)
        self.RemoveWhitelist.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(220, 95, 0); \n"
"\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.BrowseFile.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Unproductive Categories", None))
        self.groupBox_2.setTitle("")
        self.EditWhitelist.setText("")
        self.EditWhitelist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a website link or click on the 'File' button to whitelist a local file", None))
        self.BrowseFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.AddWhitelist.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Whitelisted Websites/Local Files", None))
        self.RemoveWhitelist.setText(QCoreApplication.translate("MainWindow", u"-", None))
    # retranslateUi


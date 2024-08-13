# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowYRZIee.ui'
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
        MainWindow.resize(1045, 600)
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
        self.groupBox.setGeometry(QRect(20, 20, 311, 571))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"border:none\n"
"}")
        self.groupBox.setFlat(False)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 190, 291, 381))
        self.Categories = QVBoxLayout(self.verticalLayoutWidget)
        self.Categories.setObjectName(u"Categories")
        self.Categories.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 281, 31))
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
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 291, 71))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel{\n"
"color: rgb(238, 238, 238);\n"
"}\n"
"")
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 110, 291, 71))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel{\n"
"color: rgb(238, 238, 238);\n"
"}")
        self.label_5.setWordWrap(True)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(360, 30, 671, 561))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"border:none\n"
"}")
        self.groupBox_2.setFlat(False)
        self.EditWhitelist = QLineEdit(self.groupBox_2)
        self.EditWhitelist.setObjectName(u"EditWhitelist")
        self.EditWhitelist.setGeometry(QRect(50, 40, 551, 31))
        self.EditWhitelist.setFont(font1)
        self.EditWhitelist.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.BrowseFile = QPushButton(self.groupBox_2)
        self.BrowseFile.setObjectName(u"BrowseFile")
        self.BrowseFile.setGeometry(QRect(0, 40, 41, 31))
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
        self.AddWhitelist.setGeometry(QRect(610, 40, 51, 31))
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
        self.Whitelist.setGeometry(QRect(10, 80, 611, 191))
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
        self.label_2.setGeometry(QRect(0, 0, 651, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.RemoveWhitelist = QPushButton(self.groupBox_2)
        self.RemoveWhitelist.setObjectName(u"RemoveWhitelist")
        self.RemoveWhitelist.setGeometry(QRect(630, 90, 31, 31))
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
        self.BrowseFile_2 = QPushButton(self.groupBox_2)
        self.BrowseFile_2.setObjectName(u"BrowseFile_2")
        self.BrowseFile_2.setGeometry(QRect(0, 320, 41, 31))
        self.BrowseFile_2.setFont(font2)
        self.BrowseFile_2.setLayoutDirection(Qt.LeftToRight)
        self.BrowseFile_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(104, 109, 118);\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.BrowseFile_2.setCheckable(False)
        self.AddBlacklist = QPushButton(self.groupBox_2)
        self.AddBlacklist.setObjectName(u"AddBlacklist")
        self.AddBlacklist.setGeometry(QRect(610, 320, 51, 31))
        self.AddBlacklist.setFont(font3)
        self.AddBlacklist.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(55, 58, 64);\n"
"}")
        self.AddBlacklist.setCheckable(False)
        self.AddBlacklist.setFlat(False)
        self.RemoveBlacklist = QPushButton(self.groupBox_2)
        self.RemoveBlacklist.setObjectName(u"RemoveBlacklist")
        self.RemoveBlacklist.setGeometry(QRect(630, 360, 31, 31))
        sizePolicy.setHeightForWidth(self.RemoveBlacklist.sizePolicy().hasHeightForWidth())
        self.RemoveBlacklist.setSizePolicy(sizePolicy)
        self.RemoveBlacklist.setFont(font5)
        self.RemoveBlacklist.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(220, 95, 0); \n"
"\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.EditBlacklist = QLineEdit(self.groupBox_2)
        self.EditBlacklist.setObjectName(u"EditBlacklist")
        self.EditBlacklist.setGeometry(QRect(50, 320, 551, 31))
        self.EditBlacklist.setFont(font1)
        self.EditBlacklist.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.Blacklist = QListWidget(self.groupBox_2)
        self.Blacklist.setObjectName(u"Blacklist")
        self.Blacklist.setGeometry(QRect(0, 360, 611, 201))
        self.Blacklist.setFont(font4)
        self.Blacklist.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(55, 58, 64);\n"
"}")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 290, 671, 20))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.Settings = QPushButton(self.centralwidget)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setGeometry(QRect(960, 10, 71, 31))
        self.Settings.setFont(font3)
        self.Settings.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(220, 95, 0);\n"
"color: rgb(238, 238, 238);\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.BrowseFile.setDefault(True)
        self.BrowseFile_2.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Unproductive Categories", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Check the categories that you wish to deem as 'unproductive'. Hover over the checkbox text to see examples of websites that fall under the category.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"The algorithm will then detect websites similar to those under the checked categories, and categorise them as unproductive when accessed by you.", None))
        self.groupBox_2.setTitle("")
        self.EditWhitelist.setText("")
        self.EditWhitelist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a website link or click on the 'File' button to whitelist a local file", None))
        self.BrowseFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.AddWhitelist.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Whitelisted Websites", None))
        self.RemoveWhitelist.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.BrowseFile_2.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.AddBlacklist.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.RemoveBlacklist.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.EditBlacklist.setText("")
        self.EditBlacklist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a website link or click on the 'File' button to blacklist a local file", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Blacklisted Websites", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi


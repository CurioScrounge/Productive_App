# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - CopyXuDfyG.ui'
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
        MainWindow.resize(1045, 609)
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
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.Settings = QPushButton(self.centralwidget)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setMaximumSize(QSize(70, 30))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Settings.setFont(font)
        self.Settings.setLayoutDirection(Qt.LeftToRight)
        self.Settings.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(220, 95, 0);\n"
"color: rgb(238, 238, 238);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Settings)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(17)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BrowseFile = QPushButton(self.centralwidget)
        self.BrowseFile.setObjectName(u"BrowseFile")
        self.BrowseFile.setMaximumSize(QSize(40, 30))
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

        self.horizontalLayout.addWidget(self.BrowseFile)

        self.AddWhitelist = QPushButton(self.centralwidget)
        self.AddWhitelist.setObjectName(u"AddWhitelist")
        self.AddWhitelist.setMaximumSize(QSize(50, 16777215))
        self.AddWhitelist.setFont(font)
        self.AddWhitelist.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(55, 58, 64);\n"
"}")
        self.AddWhitelist.setCheckable(False)
        self.AddWhitelist.setFlat(False)

        self.horizontalLayout.addWidget(self.AddWhitelist)

        self.EditWhitelist = QLineEdit(self.centralwidget)
        self.EditWhitelist.setObjectName(u"EditWhitelist")
        self.EditWhitelist.setMinimumSize(QSize(0, 30))
        self.EditWhitelist.setMaximumSize(QSize(167000, 16777215))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.EditWhitelist.setFont(font3)
        self.EditWhitelist.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.horizontalLayout.addWidget(self.EditWhitelist)

        self.RemoveWhitelist = QPushButton(self.centralwidget)
        self.RemoveWhitelist.setObjectName(u"RemoveWhitelist")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveWhitelist.sizePolicy().hasHeightForWidth())
        self.RemoveWhitelist.setSizePolicy(sizePolicy)
        self.RemoveWhitelist.setMaximumSize(QSize(30, 30))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setWeight(75)
        self.RemoveWhitelist.setFont(font4)
        self.RemoveWhitelist.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(220, 95, 0); \n"
"\n"
"	background-color: rgb(238, 238, 238);\n"
"}")

        self.horizontalLayout.addWidget(self.RemoveWhitelist)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.Whitelist = QListWidget(self.centralwidget)
        self.Whitelist.setObjectName(u"Whitelist")
        self.Whitelist.setMinimumSize(QSize(0, 100))
        self.Whitelist.setMaximumSize(QSize(16777215, 1000))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setItalic(False)
        self.Whitelist.setFont(font5)
        self.Whitelist.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(55, 58, 64);\n"
"}")

        self.verticalLayout_2.addWidget(self.Whitelist)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BrowseFile_2 = QPushButton(self.centralwidget)
        self.BrowseFile_2.setObjectName(u"BrowseFile_2")
        self.BrowseFile_2.setMaximumSize(QSize(40, 16777215))
        self.BrowseFile_2.setFont(font2)
        self.BrowseFile_2.setLayoutDirection(Qt.LeftToRight)
        self.BrowseFile_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(104, 109, 118);\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.BrowseFile_2.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.BrowseFile_2)

        self.AddBlacklist = QPushButton(self.centralwidget)
        self.AddBlacklist.setObjectName(u"AddBlacklist")
        self.AddBlacklist.setMaximumSize(QSize(50, 16777215))
        self.AddBlacklist.setFont(font)
        self.AddBlacklist.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(55, 58, 64);\n"
"}")
        self.AddBlacklist.setCheckable(False)
        self.AddBlacklist.setFlat(False)

        self.horizontalLayout_2.addWidget(self.AddBlacklist)

        self.EditBlacklist = QLineEdit(self.centralwidget)
        self.EditBlacklist.setObjectName(u"EditBlacklist")
        self.EditBlacklist.setMinimumSize(QSize(0, 30))
        self.EditBlacklist.setFont(font3)
        self.EditBlacklist.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.horizontalLayout_2.addWidget(self.EditBlacklist)

        self.RemoveBlacklist = QPushButton(self.centralwidget)
        self.RemoveBlacklist.setObjectName(u"RemoveBlacklist")
        sizePolicy.setHeightForWidth(self.RemoveBlacklist.sizePolicy().hasHeightForWidth())
        self.RemoveBlacklist.setSizePolicy(sizePolicy)
        self.RemoveBlacklist.setMaximumSize(QSize(30, 30))
        self.RemoveBlacklist.setFont(font4)
        self.RemoveBlacklist.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(220, 95, 0); \n"
"\n"
"	background-color: rgb(238, 238, 238);\n"
"}")

        self.horizontalLayout_2.addWidget(self.RemoveBlacklist)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.Blacklist = QListWidget(self.centralwidget)
        self.Blacklist.setObjectName(u"Blacklist")
        self.Blacklist.setMinimumSize(QSize(0, 100))
        self.Blacklist.setMaximumSize(QSize(16777215, 1000))
        self.Blacklist.setFont(font5)
        self.Blacklist.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(55, 58, 64);\n"
"}")

        self.verticalLayout_2.addWidget(self.Blacklist)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(16777215, 80))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"QLabel{\n"
"color: rgb(238, 238, 238);\n"
"}\n"
"")
        self.label_4.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(16777215, 80))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"QLabel{\n"
"color: rgb(238, 238, 238);\n"
"}")
        self.label_5.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_5)

        self.Categories = QVBoxLayout()
        self.Categories.setObjectName(u"Categories")
        self.Categories.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout.addLayout(self.Categories)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.BrowseFile.setDefault(True)
        self.BrowseFile_2.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Whitelisted Websites", None))
        self.BrowseFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.AddWhitelist.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.EditWhitelist.setText("")
        self.EditWhitelist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a website link or click on the 'File' button to whitelist a local file", None))
        self.RemoveWhitelist.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Blacklisted Websites", None))
        self.BrowseFile_2.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.AddBlacklist.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.EditBlacklist.setText("")
        self.EditBlacklist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a website link or click on the 'File' button to blacklist a local file", None))
        self.RemoveBlacklist.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Unproductive Categories", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Check the categories that you wish to deem as 'unproductive'. Hover over the checkbox text to see examples of websites that fall under the category.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"The algorithm will then detect websites similar to those under the checked categories, and categorise them as unproductive when accessed by you.", None))
    # retranslateUi


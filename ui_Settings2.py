# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings - CopyZFrqRd.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)



class Ui_Settings(object):
    def setupUi(self, Settings):
        if Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(1045, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        Settings.setFont(font)
        Settings.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(55, 58, 64);\n"
"}")
        self.centralwidget = QWidget(Settings)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.centralwidget.setFont(font1)
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(19)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 35))
        font3 = QFont()
        font3.setPointSize(15)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 35))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Start = QTimeEdit(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setMinimumSize(QSize(125, 35))
        self.Start.setMaximumSize(QSize(60, 16777215))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setWeight(75)
        self.Start.setFont(font4)
        self.Start.setStyleSheet(u"QTimeEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"	\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.Start.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.Start.setAccelerated(False)
        self.Start.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.horizontalLayout_2.addWidget(self.Start)

        self.End = QTimeEdit(self.centralwidget)
        self.End.setObjectName(u"End")
        self.End.setMinimumSize(QSize(125, 35))
        self.End.setMaximumSize(QSize(60, 16777215))
        self.End.setFont(font4)
        self.End.setStyleSheet(u"QTimeEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"	\n"
"	color: rgb(220, 95, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.End)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 35))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.verticalLayout_2.addWidget(self.label_4)

        self.monday = QCheckBox(self.centralwidget)
        self.monday.setObjectName(u"monday")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(13)
        self.monday.setFont(font6)
        self.monday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.verticalLayout_2.addWidget(self.monday)

        self.tuesday = QCheckBox(self.centralwidget)
        self.tuesday.setObjectName(u"tuesday")
        self.tuesday.setFont(font6)
        self.tuesday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.verticalLayout_2.addWidget(self.tuesday)

        self.wednesday = QCheckBox(self.centralwidget)
        self.wednesday.setObjectName(u"wednesday")
        self.wednesday.setFont(font6)
        self.wednesday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.verticalLayout_2.addWidget(self.wednesday)

        self.thursday = QCheckBox(self.centralwidget)
        self.thursday.setObjectName(u"thursday")
        self.thursday.setFont(font6)
        self.thursday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.verticalLayout_2.addWidget(self.thursday)

        self.friday = QCheckBox(self.centralwidget)
        self.friday.setObjectName(u"friday")
        self.friday.setFont(font6)
        self.friday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.verticalLayout_2.addWidget(self.friday)

        self.saturday = QCheckBox(self.centralwidget)
        self.saturday.setObjectName(u"saturday")
        self.saturday.setFont(font6)
        self.saturday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.verticalLayout_2.addWidget(self.saturday)

        self.sunday = QCheckBox(self.centralwidget)
        self.sunday.setObjectName(u"sunday")
        self.sunday.setFont(font6)
        self.sunday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.verticalLayout_2.addWidget(self.sunday)

        self.AddTiming = QPushButton(self.centralwidget)
        self.AddTiming.setObjectName(u"AddTiming")
        self.AddTiming.setMaximumSize(QSize(100, 16777215))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setWeight(50)
        self.AddTiming.setFont(font7)
        self.AddTiming.setStyleSheet(u"QPushButton{\n"
"	color: rgb(238, 238, 238);\n"
"\n"
"	background-color: rgb(104, 109, 118);\n"
"}")

        self.verticalLayout_2.addWidget(self.AddTiming)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.RemoveTiming = QPushButton(self.centralwidget)
        self.RemoveTiming.setObjectName(u"RemoveTiming")
        self.RemoveTiming.setMaximumSize(QSize(90, 16777215))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(11)
        self.RemoveTiming.setFont(font8)
        self.RemoveTiming.setStyleSheet(u"QPushButton{\n"
"	color: rgb(238, 238, 238);\n"
"\n"
"	background-color: rgb(104, 109, 118);\n"
"}")

        self.horizontalLayout_3.addWidget(self.RemoveTiming)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.ExistingRunTimes = QListWidget(self.centralwidget)
        self.ExistingRunTimes.setObjectName(u"ExistingRunTimes")
        self.ExistingRunTimes.setFont(font7)
        self.ExistingRunTimes.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"}")

        self.verticalLayout_3.addWidget(self.ExistingRunTimes)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 45))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_11)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setPointSize(11)
        self.label_12.setFont(font9)
        self.label_12.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.verticalLayout_4.addWidget(self.label_12)

        self.Warning = QTextEdit(self.centralwidget)
        self.Warning.setObjectName(u"Warning")
        self.Warning.setMaximumSize(QSize(16777215, 150))
        self.Warning.setFont(font)
        self.Warning.setFocusPolicy(Qt.ClickFocus)
        self.Warning.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(55, 58, 64);\n"
"}")

        self.verticalLayout_4.addWidget(self.Warning)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 45))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(14)
        font10.setBold(False)
        font10.setUnderline(True)
        font10.setWeight(50)
        self.label_6.setFont(font10)
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font8)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.Delay = QComboBox(self.centralwidget)
        self.Delay.setObjectName(u"Delay")
        self.Delay.setMaximumSize(QSize(70, 16777215))
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setWeight(75)
        self.Delay.setFont(font11)
        self.Delay.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(238, 238, 238);\n"
"}")

        self.horizontalLayout_5.addWidget(self.Delay)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(160, 0))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setFont(font8)
        self.label_9.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 40))
        self.label_10.setFont(font8)
        self.label_10.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_10)

        self.OverrideDelay = QCheckBox(self.centralwidget)
        self.OverrideDelay.setObjectName(u"OverrideDelay")
        self.OverrideDelay.setFont(font11)
        self.OverrideDelay.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(220, 95, 0);\n"
"}")

        self.verticalLayout_4.addWidget(self.OverrideDelay)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.Save = QPushButton(self.centralwidget)
        self.Save.setObjectName(u"Save")
        self.Save.setMaximumSize(QSize(60, 16777215))
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(9)
        self.Save.setFont(font12)
        self.Save.setStyleSheet(u"QPushButton{\n"
"	color: rgb(238, 238, 238);\n"
"\n"
"	background-color: rgb(104, 109, 118);\n"
"}")

        self.horizontalLayout_7.addWidget(self.Save)

        self.BackHome = QPushButton(self.centralwidget)
        self.BackHome.setObjectName(u"BackHome")
        self.BackHome.setMaximumSize(QSize(110, 16777215))
        self.BackHome.setFont(font8)
        self.BackHome.setStyleSheet(u"QPushButton{\n"
"	color: rgb(238, 238, 238);\n"
"\n"
"	\n"
"	background-color: rgb(220, 95, 0);\n"
"}")

        self.horizontalLayout_7.addWidget(self.BackHome)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"	border:none;\n"
"}")

        self.horizontalLayout_8.addWidget(self.groupBox_2)

        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"Run Settings", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Start Time", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"End Time", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"Days to run", None))
        self.monday.setText(QCoreApplication.translate("Settings", u"Monday", None))
        self.tuesday.setText(QCoreApplication.translate("Settings", u"Tueday", None))
        self.wednesday.setText(QCoreApplication.translate("Settings", u"Wednesday", None))
        self.thursday.setText(QCoreApplication.translate("Settings", u"Thursday", None))
        self.friday.setText(QCoreApplication.translate("Settings", u"Friday", None))
        self.saturday.setText(QCoreApplication.translate("Settings", u"Saturday", None))
        self.sunday.setText(QCoreApplication.translate("Settings", u"Sunday", None))
        self.AddTiming.setText(QCoreApplication.translate("Settings", u"Add Setting", None))
        self.label_5.setText(QCoreApplication.translate("Settings", u"Defined Run Times", None))
        self.RemoveTiming.setText(QCoreApplication.translate("Settings", u"Remove", None))
        self.label_11.setText(QCoreApplication.translate("Settings", u"Warning Message", None))
        self.label_12.setText(QCoreApplication.translate("Settings", u"Edit warning message:", None))
        self.Warning.setHtml(QCoreApplication.translate("Settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Settings", u"Warning Message Delay Period", None))
        self.label_7.setText(QCoreApplication.translate("Settings", u"The program will wait until there has been", None))
        self.label_8.setText(QCoreApplication.translate("Settings", u"minutes of continuous", None))
        self.label_9.setText(QCoreApplication.translate("Settings", u"unproductive activity before warning you.", None))
        self.label_10.setText(QCoreApplication.translate("Settings", u"OR immediately show warning message upon unproductive activity:", None))
        self.OverrideDelay.setText(QCoreApplication.translate("Settings", u"Override Delay Period", None))
        self.Save.setText(QCoreApplication.translate("Settings", u"Save", None))
        self.BackHome.setText(QCoreApplication.translate("Settings", u"Back to Home", None))
        self.groupBox_2.setTitle("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingskDgNjW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)



class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(974, 677)
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
        self.ExistingRunTimes = QListWidget(self.centralwidget)
        self.ExistingRunTimes.setObjectName(u"ExistingRunTimes")
        self.ExistingRunTimes.setGeometry(QRect(360, 100, 301, 551))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.ExistingRunTimes.setFont(font2)
        self.ExistingRunTimes.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 331, 641))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"")
        self.groupBox.setFlat(False)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 301, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(19)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 90, 291, 111))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(20)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(15)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_2)

        self.Start = QTimeEdit(self.verticalLayoutWidget)
        self.Start.setObjectName(u"Start")
        self.Start.setMinimumSize(QSize(125, 35))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setWeight(75)
        self.Start.setFont(font5)
        self.Start.setStyleSheet(u"QTimeEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"	\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.Start.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.Start.setAccelerated(False)
        self.Start.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Start)

        self.End = QTimeEdit(self.verticalLayoutWidget)
        self.End.setObjectName(u"End")
        self.End.setMinimumSize(QSize(125, 35))
        self.End.setFont(font5)
        self.End.setStyleSheet(u"QTimeEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"	\n"
"	color: rgb(220, 95, 0);\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.End)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)


        self.verticalLayout.addLayout(self.formLayout)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 220, 181, 31))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(15)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.monday = QCheckBox(self.groupBox)
        self.monday.setObjectName(u"monday")
        self.monday.setGeometry(QRect(30, 280, 121, 21))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        self.monday.setFont(font7)
        self.monday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.tuesday = QCheckBox(self.groupBox)
        self.tuesday.setObjectName(u"tuesday")
        self.tuesday.setGeometry(QRect(30, 320, 121, 21))
        self.tuesday.setFont(font7)
        self.tuesday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.wednesday = QCheckBox(self.groupBox)
        self.wednesday.setObjectName(u"wednesday")
        self.wednesday.setGeometry(QRect(30, 360, 121, 21))
        self.wednesday.setFont(font7)
        self.wednesday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.thursday = QCheckBox(self.groupBox)
        self.thursday.setObjectName(u"thursday")
        self.thursday.setGeometry(QRect(30, 400, 121, 21))
        self.thursday.setFont(font7)
        self.thursday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.friday = QCheckBox(self.groupBox)
        self.friday.setObjectName(u"friday")
        self.friday.setGeometry(QRect(30, 440, 121, 21))
        self.friday.setFont(font7)
        self.friday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.saturday = QCheckBox(self.groupBox)
        self.saturday.setObjectName(u"saturday")
        self.saturday.setGeometry(QRect(30, 480, 121, 21))
        self.saturday.setFont(font7)
        self.saturday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.sunday = QCheckBox(self.groupBox)
        self.sunday.setObjectName(u"sunday")
        self.sunday.setGeometry(QRect(30, 520, 121, 21))
        self.sunday.setFont(font7)
        self.sunday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.AddTiming = QPushButton(self.groupBox)
        self.AddTiming.setObjectName(u"AddTiming")
        self.AddTiming.setGeometry(QRect(30, 570, 101, 31))
        self.AddTiming.setFont(font2)
        self.AddTiming.setStyleSheet(u"QPushButton{\n"
"	color: rgb(238, 238, 238);\n"
"\n"
"	background-color: rgb(104, 109, 118);\n"
"}")
        self.RemoveTiming = QPushButton(self.centralwidget)
        self.RemoveTiming.setObjectName(u"RemoveTiming")
        self.RemoveTiming.setGeometry(QRect(640, 60, 81, 31))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(11)
        self.RemoveTiming.setFont(font8)
        self.RemoveTiming.setStyleSheet(u"QPushButton{\n"
"	color: rgb(238, 238, 238);\n"
"\n"
"	background-color: rgb(104, 109, 118);\n"
"}")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 30, 301, 41))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(680, 110, 281, 491))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"	border-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 10, 251, 81))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.Delay = QComboBox(self.groupBox_2)
        self.Delay.addItem("")
        self.Delay.setObjectName(u"Delay")
        self.Delay.setGeometry(QRect(40, 150, 51, 31))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setWeight(75)
        self.Delay.setFont(font9)
        self.Delay.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 110, 251, 31))
        self.label_7.setFont(font8)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_7.setWordWrap(True)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 150, 161, 31))
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_8.setWordWrap(True)
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 190, 251, 41))
        self.label_9.setFont(font8)
        self.label_9.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_9.setWordWrap(True)
        self.BackHome = QPushButton(self.centralwidget)
        self.BackHome.setObjectName(u"BackHome")
        self.BackHome.setGeometry(QRect(850, 630, 111, 31))
        self.BackHome.setFont(font8)
        self.BackHome.setStyleSheet(u"QPushButton{\n"
"	color: rgb(238, 238, 238);\n"
"\n"
"	\n"
"	background-color: rgb(220, 95, 0);\n"
"}")
        Settings.setCentralWidget(self.centralwidget)
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.ExistingRunTimes.raise_()
        self.label_5.raise_()
        self.RemoveTiming.raise_()
        self.BackHome.raise_()

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Settings", u"Run Settings", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"End Time", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Start Time", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"Days to run", None))
        self.monday.setText(QCoreApplication.translate("Settings", u"Monday", None))
        self.tuesday.setText(QCoreApplication.translate("Settings", u"Tueday", None))
        self.wednesday.setText(QCoreApplication.translate("Settings", u"Wednesday", None))
        self.thursday.setText(QCoreApplication.translate("Settings", u"Thursday", None))
        self.friday.setText(QCoreApplication.translate("Settings", u"Friday", None))
        self.saturday.setText(QCoreApplication.translate("Settings", u"Saturday", None))
        self.sunday.setText(QCoreApplication.translate("Settings", u"Sunday", None))
        self.AddTiming.setText(QCoreApplication.translate("Settings", u"Add Setting", None))
        self.RemoveTiming.setText(QCoreApplication.translate("Settings", u"Remove", None))
        self.label_5.setText(QCoreApplication.translate("Settings", u"Defined Run Times", None))
        self.groupBox_2.setTitle("")
        self.label_6.setText(QCoreApplication.translate("Settings", u"Warning Message Delay Period", None))
        self.Delay.setItemText(0, QCoreApplication.translate("Settings", u"5", None))

        self.label_7.setText(QCoreApplication.translate("Settings", u"The program will until there has been", None))
        self.label_8.setText(QCoreApplication.translate("Settings", u"minutes of continuous", None))
        self.label_9.setText(QCoreApplication.translate("Settings", u"unproductive activity before warning you.", None))
        self.BackHome.setText(QCoreApplication.translate("Settings", u"Back to Home", None))
    # retranslateUi


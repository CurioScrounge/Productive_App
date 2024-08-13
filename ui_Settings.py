# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsgVjgoa.ui'
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
        self.ExistingRunTimes = QListWidget(self.centralwidget)
        self.ExistingRunTimes.setObjectName(u"ExistingRunTimes")
        self.ExistingRunTimes.setGeometry(QRect(340, 100, 341, 491))
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
        self.groupBox.setGeometry(QRect(10, 10, 321, 571))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border:none;\n"
"}\n"
"\n"
"")
        self.groupBox.setFlat(False)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 301, 41))
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
        self.verticalLayoutWidget.setGeometry(QRect(20, 70, 291, 91))
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
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(15)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

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

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 170, 181, 31))
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
        self.monday.setGeometry(QRect(30, 220, 121, 21))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(13)
        self.monday.setFont(font7)
        self.monday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.tuesday = QCheckBox(self.groupBox)
        self.tuesday.setObjectName(u"tuesday")
        self.tuesday.setGeometry(QRect(30, 260, 121, 21))
        self.tuesday.setFont(font7)
        self.tuesday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.wednesday = QCheckBox(self.groupBox)
        self.wednesday.setObjectName(u"wednesday")
        self.wednesday.setGeometry(QRect(30, 300, 121, 21))
        self.wednesday.setFont(font7)
        self.wednesday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.thursday = QCheckBox(self.groupBox)
        self.thursday.setObjectName(u"thursday")
        self.thursday.setGeometry(QRect(30, 340, 121, 21))
        self.thursday.setFont(font7)
        self.thursday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.friday = QCheckBox(self.groupBox)
        self.friday.setObjectName(u"friday")
        self.friday.setGeometry(QRect(30, 380, 121, 21))
        self.friday.setFont(font7)
        self.friday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.saturday = QCheckBox(self.groupBox)
        self.saturday.setObjectName(u"saturday")
        self.saturday.setGeometry(QRect(30, 420, 121, 21))
        self.saturday.setFont(font7)
        self.saturday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.sunday = QCheckBox(self.groupBox)
        self.sunday.setObjectName(u"sunday")
        self.sunday.setGeometry(QRect(30, 460, 121, 21))
        self.sunday.setFont(font7)
        self.sunday.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.AddTiming = QPushButton(self.groupBox)
        self.AddTiming.setObjectName(u"AddTiming")
        self.AddTiming.setGeometry(QRect(30, 510, 101, 31))
        self.AddTiming.setFont(font2)
        self.AddTiming.setStyleSheet(u"QPushButton{\n"
"	color: rgb(238, 238, 238);\n"
"\n"
"	background-color: rgb(104, 109, 118);\n"
"}")
        self.RemoveTiming = QPushButton(self.centralwidget)
        self.RemoveTiming.setObjectName(u"RemoveTiming")
        self.RemoveTiming.setGeometry(QRect(590, 60, 81, 31))
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
        self.label_5.setGeometry(QRect(350, 10, 321, 41))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(690, 10, 341, 621))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"	border:none;\n"
"}")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 240, 321, 31))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(14)
        font9.setBold(False)
        font9.setUnderline(True)
        font9.setWeight(50)
        self.label_6.setFont(font9)
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.Delay = QComboBox(self.groupBox_2)
        self.Delay.setObjectName(u"Delay")
        self.Delay.setGeometry(QRect(60, 320, 51, 31))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setWeight(75)
        self.Delay.setFont(font10)
        self.Delay.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 280, 281, 21))
        self.label_7.setFont(font8)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_7.setWordWrap(True)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 320, 161, 21))
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_8.setWordWrap(True)
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 360, 281, 21))
        self.label_9.setFont(font8)
        self.label_9.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_9.setWordWrap(True)
        self.OverrideDelay = QCheckBox(self.groupBox_2)
        self.OverrideDelay.setObjectName(u"OverrideDelay")
        self.OverrideDelay.setGeometry(QRect(20, 490, 231, 41))
        self.OverrideDelay.setFont(font10)
        self.OverrideDelay.setStyleSheet(u"QCheckBox{\n"
"	\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 420, 281, 41))
        self.label_10.setFont(font8)
        self.label_10.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.label_10.setWordWrap(True)
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(-10, 0, 361, 41))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"QLabel{\n"
"	color: rgb(220, 95, 0);\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.Warning = QTextEdit(self.groupBox_2)
        self.Warning.setObjectName(u"Warning")
        self.Warning.setGeometry(QRect(10, 90, 321, 141))
        self.Warning.setFont(font)
        self.Warning.setFocusPolicy(Qt.ClickFocus)
        self.Warning.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(55, 58, 64);\n"
"}")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 60, 261, 20))
        font11 = QFont()
        font11.setPointSize(11)
        self.label_12.setFont(font11)
        self.label_12.setStyleSheet(u"QLabel{\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.Save = QPushButton(self.groupBox_2)
        self.Save.setObjectName(u"Save")
        self.Save.setGeometry(QRect(150, 550, 61, 31))
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(9)
        self.Save.setFont(font12)
        self.Save.setStyleSheet(u"QPushButton{\n"
"	color: rgb(238, 238, 238);\n"
"\n"
"	background-color: rgb(104, 109, 118);\n"
"}")
        self.BackHome = QPushButton(self.groupBox_2)
        self.BackHome.setObjectName(u"BackHome")
        self.BackHome.setGeometry(QRect(230, 550, 111, 31))
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

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"MainWindow", None))
        self.groupBox.setTitle("")
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
        self.RemoveTiming.setText(QCoreApplication.translate("Settings", u"Remove", None))
        self.label_5.setText(QCoreApplication.translate("Settings", u"Defined Run Times", None))
        self.groupBox_2.setTitle("")
        self.label_6.setText(QCoreApplication.translate("Settings", u"Warning Message Delay Period", None))
        self.label_7.setText(QCoreApplication.translate("Settings", u"The program will wait until there has been", None))
        self.label_8.setText(QCoreApplication.translate("Settings", u"minutes of continuous", None))
        self.label_9.setText(QCoreApplication.translate("Settings", u"unproductive activity before warning you.", None))
        self.OverrideDelay.setText(QCoreApplication.translate("Settings", u"Override Delay Period", None))
        self.label_10.setText(QCoreApplication.translate("Settings", u"OR immediately show warning message upon unproductive activity:", None))
        self.label_11.setText(QCoreApplication.translate("Settings", u"Warning Message", None))
        self.Warning.setHtml(QCoreApplication.translate("Settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Settings", u"Edit warning message:", None))
        self.Save.setText(QCoreApplication.translate("Settings", u"Save", None))
        self.BackHome.setText(QCoreApplication.translate("Settings", u"Back to Home", None))
    # retranslateUi


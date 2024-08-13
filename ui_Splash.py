# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashSdXavP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(931, 574)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setPointSize(30)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"QFrame{\n"
" \n"
"	background-color: rgb(55, 58, 64);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 160, 911, 91))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(36)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 116, 70);\n"
"}\n"
"")
        self.label_title.setTextFormat(Qt.AutoText)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(90, 460, 731, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"text-align:center;\n"
"	background-color: rgb(238, 238, 238);\n"
"color:rgb(55, 58, 64);\n"
"border-style:none;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.489, stop:0 rgba(220, 95, 0, 255), stop:1 rgba(204, 68, 0, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_phrase = QLabel(self.frame)
        self.label_phrase.setObjectName(u"label_phrase")
        self.label_phrase.setGeometry(QRect(10, 240, 891, 51))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_phrase.setFont(font2)
        self.label_phrase.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_phrase.setTextFormat(Qt.AutoText)
        self.label_phrase.setAlignment(Qt.AlignCenter)
        self.label_status = QLabel(self.frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(10, 490, 901, 51))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_status.setFont(font3)
        self.label_status.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_status.setTextFormat(Qt.AutoText)
        self.label_status.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.frame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(640, 500, 261, 51))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_credits.setFont(font4)
        self.label_credits.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_credits.setTextFormat(Qt.AutoText)
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_phrase.raise_()
        self.label_title.raise_()
        self.progressBar.raise_()
        self.label_status.raise_()
        self.label_credits.raise_()

        self.verticalLayout.addWidget(self.frame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600; color:#dc5f00;\">UNLEASH</span><span style=\" color:#dc5f00;\"> YOUR PRODUCTIVE POTENTIAL</span></p></body></html>", None))
        self.label_phrase.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Greatly customisable to your benefit, maximise your productivity today!</span></p></body></html>", None))
        self.label_status.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<strong>Created by:</strong> Summer Guo", None))
    # retranslateUi


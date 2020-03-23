# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject, Qt
from PyQt5.QtWidgets import QLabel, QWidget, QSplitter, QMenuBar, QStatusBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(100, 10, 200, 31))
        font = QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setGeometry(QRect(20, 70, 351, 151))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_2 = QLabel(self.splitter)
        font = QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_22")
        self.label_3 = QLabel(self.splitter)
        font = QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Новая вкладка"))
        self.label.setText(_translate("MainWindow", "Добро Пожаловать"))
        self.label_2.setText(_translate("MainWindow", "Чтобы начать нажмите PgUp."))
        self.label_3.setText(_translate("MainWindow", "Чтобы завершить нажмите PgUp и подождите."))

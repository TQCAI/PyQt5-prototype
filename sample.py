# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sample(object):
    def setupUi(self, Sample):
        Sample.setObjectName("Sample")
        Sample.resize(800, 600)
        Sample.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(Sample)
        self.centralwidget.setObjectName("centralwidget")
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setGeometry(QtCore.QRect(10, 250, 781, 301))
        self.bottom.setFrameShape(QtWidgets.QFrame.Box)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bottom.setObjectName("bottom")
        self.button_2 = QtWidgets.QPushButton(self.bottom)
        self.button_2.setGeometry(QtCore.QRect(90, 110, 111, 26))
        self.button_2.setObjectName("button_2")
        self.button_1 = QtWidgets.QPushButton(self.bottom)
        self.button_1.setGeometry(QtCore.QRect(90, 80, 111, 26))
        self.button_1.setObjectName("button_1")
        self.top_right = QtWidgets.QTextEdit(self.centralwidget)
        self.top_right.setGeometry(QtCore.QRect(330, 10, 461, 241))
        self.top_right.setObjectName("top_right")
        Sample.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Sample)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Sample.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Sample)
        self.statusbar.setObjectName("statusbar")
        Sample.setStatusBar(self.statusbar)

        self.retranslateUi(Sample)
        QtCore.QMetaObject.connectSlotsByName(Sample)

    def retranslateUi(self, Sample):
        _translate = QtCore.QCoreApplication.translate
        Sample.setWindowTitle(_translate("Sample", "Sample"))
        self.button_2.setText(_translate("Sample", "open subWindow"))
        self.button_1.setText(_translate("Sample", "open dialog"))


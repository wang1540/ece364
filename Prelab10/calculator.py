# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ecegrid/a/ee364b09/Prelab10/calculator.ui'
#
# Created: Thu Mar 26 19:45:10 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 410)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.disline = QtGui.QLineEdit(self.centralwidget)
        self.disline.setGeometry(QtCore.QRect(60, 50, 481, 41))
        self.disline.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.disline.setFrame(True)
        self.disline.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.disline.setObjectName("disline")
        self.num7 = QtGui.QPushButton(self.centralwidget)
        self.num7.setGeometry(QtCore.QRect(60, 110, 91, 31))
        self.num7.setObjectName("num7")
        self.num8 = QtGui.QPushButton(self.centralwidget)
        self.num8.setGeometry(QtCore.QRect(160, 110, 91, 31))
        self.num8.setObjectName("num8")
        self.num9 = QtGui.QPushButton(self.centralwidget)
        self.num9.setGeometry(QtCore.QRect(260, 110, 91, 31))
        self.num9.setObjectName("num9")
        self.signdiv = QtGui.QPushButton(self.centralwidget)
        self.signdiv.setGeometry(QtCore.QRect(360, 110, 91, 31))
        self.signdiv.setObjectName("signdiv")
        self.signmul = QtGui.QPushButton(self.centralwidget)
        self.signmul.setGeometry(QtCore.QRect(360, 150, 91, 31))
        self.signmul.setObjectName("signmul")
        self.num6 = QtGui.QPushButton(self.centralwidget)
        self.num6.setGeometry(QtCore.QRect(260, 150, 91, 31))
        self.num6.setObjectName("num6")
        self.num5 = QtGui.QPushButton(self.centralwidget)
        self.num5.setGeometry(QtCore.QRect(160, 150, 91, 31))
        self.num5.setObjectName("num5")
        self.num4 = QtGui.QPushButton(self.centralwidget)
        self.num4.setGeometry(QtCore.QRect(60, 150, 91, 31))
        self.num4.setObjectName("num4")
        self.signmin = QtGui.QPushButton(self.centralwidget)
        self.signmin.setGeometry(QtCore.QRect(360, 190, 91, 31))
        self.signmin.setObjectName("signmin")
        self.num3 = QtGui.QPushButton(self.centralwidget)
        self.num3.setGeometry(QtCore.QRect(260, 190, 91, 31))
        self.num3.setObjectName("num3")
        self.num2 = QtGui.QPushButton(self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(160, 190, 91, 31))
        self.num2.setObjectName("num2")
        self.num1 = QtGui.QPushButton(self.centralwidget)
        self.num1.setGeometry(QtCore.QRect(60, 190, 91, 31))
        self.num1.setObjectName("num1")
        self.signadd = QtGui.QPushButton(self.centralwidget)
        self.signadd.setGeometry(QtCore.QRect(360, 230, 91, 31))
        self.signadd.setObjectName("signadd")
        self.dot = QtGui.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(260, 230, 91, 31))
        self.dot.setObjectName("dot")
        self.num0 = QtGui.QPushButton(self.centralwidget)
        self.num0.setGeometry(QtCore.QRect(60, 230, 191, 31))
        self.num0.setObjectName("num0")
        self.signdel = QtGui.QPushButton(self.centralwidget)
        self.signdel.setGeometry(QtCore.QRect(460, 110, 81, 71))
        self.signdel.setObjectName("signdel")
        self.signequ = QtGui.QPushButton(self.centralwidget)
        self.signequ.setGeometry(QtCore.QRect(460, 190, 81, 71))
        self.signequ.setObjectName("signequ")
        self.diglabel = QtGui.QLabel(self.centralwidget)
        self.diglabel.setGeometry(QtCore.QRect(60, 290, 111, 17))
        self.diglabel.setObjectName("diglabel")
        self.septhousand = QtGui.QCheckBox(self.centralwidget)
        self.septhousand.setGeometry(QtCore.QRect(290, 290, 231, 22))
        self.septhousand.setAutoFillBackground(True)
        self.septhousand.setChecked(True)
        self.septhousand.setObjectName("septhousand")
        self.numdigits = QtGui.QComboBox(self.centralwidget)
        self.numdigits.setGeometry(QtCore.QRect(180, 280, 85, 27))
        self.numdigits.setObjectName("numdigits")
        self.numdigits.addItem("")
        self.numdigits.addItem("")
        self.numdigits.addItem("")
        self.numdigits.addItem("")
        self.numdigits.addItem("")
        self.numdigits.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.numdigits.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.disline.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.num7.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.num8.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.num9.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.signdiv.setText(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.signmul.setText(QtGui.QApplication.translate("MainWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.num6.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.num5.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.num4.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.signmin.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.num3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.num2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.num1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.signadd.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.dot.setText(QtGui.QApplication.translate("MainWindow", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.num0.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.signdel.setText(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.signequ.setText(QtGui.QApplication.translate("MainWindow", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.diglabel.setText(QtGui.QApplication.translate("MainWindow", "Decimal Digits", None, QtGui.QApplication.UnicodeUTF8))
        self.septhousand.setText(QtGui.QApplication.translate("MainWindow", "Display Thousands\' Separator", None, QtGui.QApplication.UnicodeUTF8))
        self.numdigits.setItemText(0, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.numdigits.setItemText(1, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.numdigits.setItemText(2, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.numdigits.setItemText(3, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.numdigits.setItemText(4, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.numdigits.setItemText(5, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ecegrid/a/ee364b09/Lab11/SteganographyGUI.ui'
#
# Created: Tue Apr 14 11:35:59 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 411)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grpMedium = QtGui.QGroupBox(self.centralwidget)
        self.grpMedium.setGeometry(QtCore.QRect(210, 10, 301, 351))
        self.grpMedium.setObjectName("grpMedium")
        self.viewMedium = QtGui.QGraphicsView(self.grpMedium)
        self.viewMedium.setGeometry(QtCore.QRect(10, 40, 281, 261))
        self.viewMedium.setObjectName("viewMedium")
        self.layoutWidget = QtGui.QWidget(self.grpMedium)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 310, 261, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnExtract = QtGui.QPushButton(self.layoutWidget)
        self.btnExtract.setObjectName("btnExtract")
        self.horizontalLayout.addWidget(self.btnExtract)
        self.btnWipeMedium = QtGui.QPushButton(self.layoutWidget)
        self.btnWipeMedium.setObjectName("btnWipeMedium")
        self.horizontalLayout.addWidget(self.btnWipeMedium)
        self.grpFiles = QtGui.QGroupBox(self.centralwidget)
        self.grpFiles.setGeometry(QtCore.QRect(10, 10, 191, 351))
        self.grpFiles.setObjectName("grpFiles")
        self.fileTreeWidget = QtGui.QTreeWidget(self.grpFiles)
        self.fileTreeWidget.setGeometry(QtCore.QRect(10, 40, 171, 301))
        self.fileTreeWidget.setObjectName("fileTreeWidget")
        self.grpMessage = QtGui.QGroupBox(self.centralwidget)
        self.grpMessage.setGeometry(QtCore.QRect(530, 10, 351, 351))
        self.grpMessage.setObjectName("grpMessage")
        self.stackMessage = QtGui.QStackedWidget(self.grpMessage)
        self.stackMessage.setGeometry(QtCore.QRect(20, 20, 321, 311))
        self.stackMessage.setAutoFillBackground(False)
        self.stackMessage.setFrameShape(QtGui.QFrame.NoFrame)
        self.stackMessage.setObjectName("stackMessage")
        self.pgImage = QtGui.QWidget()
        self.pgImage.setObjectName("pgImage")
        self.viewMessage = QtGui.QGraphicsView(self.pgImage)
        self.viewMessage.setGeometry(QtCore.QRect(10, 20, 281, 261))
        self.viewMessage.setObjectName("viewMessage")
        self.lblImageMessage = QtGui.QLabel(self.pgImage)
        self.lblImageMessage.setGeometry(QtCore.QRect(120, 290, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.lblImageMessage.setFont(font)
        self.lblImageMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblImageMessage.setObjectName("lblImageMessage")
        self.stackMessage.addWidget(self.pgImage)
        self.pgText = QtGui.QWidget()
        self.pgText.setObjectName("pgText")
        self.txtMessage = QtGui.QPlainTextEdit(self.pgText)
        self.txtMessage.setGeometry(QtCore.QRect(10, 20, 281, 261))
        self.txtMessage.setObjectName("txtMessage")
        self.lblTextMessage = QtGui.QLabel(self.pgText)
        self.lblTextMessage.setGeometry(QtCore.QRect(120, 290, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.lblTextMessage.setFont(font)
        self.lblTextMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTextMessage.setObjectName("lblTextMessage")
        self.stackMessage.addWidget(self.pgText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackMessage.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.grpMedium.setTitle(QtGui.QApplication.translate("MainWindow", "Steganography Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExtract.setText(QtGui.QApplication.translate("MainWindow", "Extract Message", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWipeMedium.setText(QtGui.QApplication.translate("MainWindow", "Wipe Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.grpFiles.setTitle(QtGui.QApplication.translate("MainWindow", "File Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "<FolderName>", None, QtGui.QApplication.UnicodeUTF8))
        self.grpMessage.setTitle(QtGui.QApplication.translate("MainWindow", "Steganography Message", None, QtGui.QApplication.UnicodeUTF8))
        self.lblImageMessage.setText(QtGui.QApplication.translate("MainWindow", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTextMessage.setText(QtGui.QApplication.translate("MainWindow", "Text", None, QtGui.QApplication.UnicodeUTF8))


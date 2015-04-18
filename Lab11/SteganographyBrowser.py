__author__ = 'Xihui Wang'

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from SteganographyGUI import *
from NewSteganography import *
import glob
import os


class SteganographyBrowser(QMainWindow, Ui_MainWindow):

    # initialize the class. 1. choose the file path 2. take all gray image files, check if they embedded with message
    # if so, then make a sub line(display type) under the file name line. display all the files with diff colors.
    def __init__(self, parent=None):
        super(SteganographyBrowser, self).__init__(parent)
        self.setupUi(self)

        self.path = QtGui.QFileDialog.getExistingDirectory()
        if not self.path:
            exit()
        foldername = self.path.split('/')[-1]
        self.fileTreeWidget.setHeaderLabel(foldername)
        filelist = glob.glob(self.path + '/*.png')

        items = []
        for files in filelist:
            # the try-except part prevent color image from adding into the widget
            try:
                stegan = NewSteganography(files)
                exist, ttype = stegan.checkIfMessageExists()
                direction = 'horizontal'
                if exist is False:
                    direction = 'vertical'
                    stegan = NewSteganography(files, 'vertical')
                    exist, ttype = stegan.checkIfMessageExists()

                item = QTreeWidgetItem(self.fileTreeWidget)
                name = files.split('/')[-1]
                item.setText(0, name)

                if exist is False:
                    item.setForeground(0, QBrush(QColor(0, 0, 255)))
                else:
                    item.setForeground(0, QBrush(QColor(255, 0, 0)))
                    foont = QtGui.QFont()
                    foont.setBold(True)
                    item.setFont(0, foont)

                    son = QTreeWidgetItem(item)
                    son.setText(0, ttype)
                    son.setText(1, direction)
                    son.setForeground(0, QBrush(QColor(0, 255, 0)))
                items += [item]
            except:
                pass
        self.fileTreeWidget.addTopLevelItems(items)
        self.mode(False)

        self.fileTreeWidget.itemClicked.connect(self.display)
        self.btnExtract.clicked.connect(self.extract)
        self.btnWipeMedium.clicked.connect(self.wipe)

    # one user clicked the file name displayed in the widget, then display the image, and enable or disable exact & wipe
    # button based on whether or not the image contains message
    def display(self):
        item = self.fileTreeWidget.currentItem()
        self.imagepath = self.path + '/' + item.text(0)

        scene = QtGui.QGraphicsScene()
        pix = QtGui.QPixmap(self.imagepath)
        scene.addPixmap(pix)
        self.viewMedium.setScene(scene)
        self.viewMedium.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)

        try:
            subitem = item.child(0)
            print(subitem.text(0))
            self.mode(True)
        except:
            self.stackMessage.setCurrentWidget(self.pgText)
            self.mode(False)

    # extract the message once user clicked the extract button. if message is in text type, then switch to text page,
    # if message is image type, then switch to image page, then display message
    def extract(self):
        self.btnExtract.setEnabled(False)

        item = self.fileTreeWidget.currentItem()
        subitem = item.child(0)
        ttypte = subitem.text(0)
        dir = subitem.text(1)

        stegan = Steganography(self.imagepath, direction=dir)
        mess = stegan.extractMessageFromMedium()

        if ttypte == 'Text':
            self.stackMessage.setCurrentWidget(self.pgText)
            mess.saveToTextFile('temp.txt')
            with open('temp.txt', 'r') as f:
                lines = f.read()
            self.txtMessage.setPlainText(lines)
            os.remove('temp.txt')
        else:
            self.stackMessage.setCurrentWidget(self.pgImage)
            mess.saveToImage('temp.png')
            scene = QtGui.QGraphicsScene()
            pix = QtGui.QPixmap('temp.png')
            scene.addPixmap(pix)
            self.viewMessage.setScene(scene)
            self.viewMessage.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
            os.remove('temp.png')

    # once user clicked wipe button, pop out the message ask user whether or not he want to wipe the message. if no,
    # then do nothing. if yes, then wipe the message and replace with its original file.
    def wipe(self):
        rest = QtGui.QMessageBox.question(self, 'title', 'message', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if rest == QtGui.QMessageBox.Yes:
            self.mode(False)
            item = self.fileTreeWidget.currentItem()
            subitem = item.child(0)
            dir = subitem.text(1)
            stegan = NewSteganography(self.imagepath, direction=dir)
            stegan.wipeMedium()
            item.removeChild(subitem)

            item.setForeground(0, QBrush(QColor(0, 0, 255)))
            foont = QtGui.QFont()
            foont.setBold(False)
            item.setFont(0, foont)

    # enable or disable the buttons, message display window
    def mode(self, require):
        self.btnExtract.setEnabled(require)
        self.btnWipeMedium.setEnabled(require)
        self.stackMessage.setEnabled(require)
        self.grpMessage.setEnabled(require)
        self.txtMessage.clear()
        scene = QtGui.QGraphicsScene()
        scene.addText('')
        self.viewMessage.setScene(scene)

currentApp = QApplication(sys.argv)
currentForm = SteganographyBrowser()

currentForm.show()
currentApp.exec_()
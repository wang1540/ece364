__author__ = 'Xihui Wang'

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from SteganographyGUI import *
from NewSteganography import *
import glob


class SteganographyBrowser(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(SteganographyBrowser, self).__init__(parent)
        self.setupUi(self)


        self.path = QtGui.QFileDialog.getExistingDirectory()
        if not self.path:
            exit()
        # print(self.path)
        foldername = self.path.split('/')[-1]
        # print(foldername)
        self.fileTreeWidget.setHeaderLabel(foldername)
        filelist = glob.glob(self.path + '/*.png')
        # print(filelist)


        # treeWidget = self.fileTreeWidget
        # treeWidget.setColumnCount(1)
        items = []
        for files in filelist:
            # the try-except part prevent color image from adding into the widget
            try:
                stegan = NewSteganography(files)
                # print(files)
                exist, ttype = stegan.checkIfMessageExists()
                if exist is False:
                    stegan = NewSteganography(files, 'vertical')
                    exist, ttype = stegan.checkIfMessageExists()

                item = QTreeWidgetItem(self.fileTreeWidget)
                name = files.split('/')[-1]
                # name = re.findall(r'/.*/(.*?\.png)', files)
                # print(name)
                # print(files)
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
                    son.setForeground(0, QBrush(QColor(0, 255, 0)))
                items += [item]
            except:
                pass
        #
        self.fileTreeWidget.addTopLevelItems(items)
        self.mode(False)

        self.fileTreeWidget.itemClicked.connect(self.display)

    def display(self):
        item = self.fileTreeWidget.currentItem()
        imagepath = self.path + '/' + item.text(0)
        # print(imagepath)
        # image = Image.open(imagepath)
        # pix = image.getdata()

        scene = QtGui.QGraphicsScene()
        pix = QtGui.QPixmap(imagepath)
        scene.addPixmap(pix)
        self.viewMedium.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        self.viewMedium.setScene(scene)

        try:
            subitem = item.child(0)
            # print(subitem.text(0))
            self.mode(True)
        except:
            self.mode(False)

    def mode(self, require):
        self.btnExtract.setEnabled(require)
        self.btnWipeMedium.setEnabled(require)
        self.stackMessage.setEnabled(require)
        self.grpMessage.setEnabled(require)



currentApp = QApplication(sys.argv)
currentForm = SteganographyBrowser()

currentForm.show()
currentApp.exec_()

# Import PySide classes

import sys
from PySide.QtCore import *
from PySide.QtGui import *

from test import *

class ConsumerApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(ConsumerApp, self).__init__(parent)
        self.setupUi(self)

        self.comboBox.currentIndexChanged.connect(self.display)

    def display(self):
        message = self.comboBox.currentText()
        self.label.setText(message)

currentApp = QApplication(sys.argv)
currentForm = ConsumerApp()

currentForm.show()
currentApp.exec_()

#! /usr/bin/env python3.4
__author__ = "Xihui Wang"

import sys
import re
from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *

class simpleCalc(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(simpleCalc, self).__init__(parent)
        self.setupUi(self)

        self.eq = 1

        inlist = [self.num0, self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.dot, self.signadd, self.signmin, self.signmul, self.signdiv]
        for ele in inlist:
            ele.clicked.connect(self.modifyinput)
        self.signdel.clicked.connect(self.delete)
        self.signequ.clicked.connect(self.equal)
        # self.septhousand.stateChanged.connect(self.modifythousand)
        # self.numdigits.currentIndexChanged.connect(self.moddig)


    def modifyinput(self):
        numbutt = self.sender()

        if self.eq == 0:
            temp = self.disline.text()
            self.disline.setText(temp + numbutt.text())
        else:
            self.disline.setText(numbutt.text())
            self.eq = 0

    def delete(self):
        temp = self.disline.text()
        self.disline.setText(temp[:-1])

    def equal(self):
        self.eq = 1
        inputstr = self.disline.text()

        addparts = inputstr.split('+')
        out = self.adder()




    def adder(self):
        mins()
    def mins(self):
        mul()
    def mul(self):
        div()

    def div(self, a):
        divparts = a.split('/')
        value = float(divparts[0])
        for i in range(len(divparts)):
            value = value / float(divparts[i + 1])
        return value

        # for addpart in addparts:
        #     minparts = addpart.split('-')
        #     # minlist = [ele for ele in minparts] if not len(minparts)==1 else []
        #     # value = float(minlist[0]) - float(minlist[1])
        #     for minpart in minparts:
        #         mulpart =


currentApp = QApplication(sys.argv)
currentForm = simpleCalc()

currentForm.show()
currentApp.exec_()
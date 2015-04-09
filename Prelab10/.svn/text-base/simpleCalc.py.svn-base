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

        self.old = None
        self.new = None
        self.stored = None

        self.prevflag = ''
        self.flag = ''
        self.eq = 0
        self.dflag = 0

        self.thousand = 1
        self.num = 0

        numlist = [self.num0, self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9]
        for numbutt in numlist:
            numbutt.clicked.connect(self.modifynum)

        self.dot.clicked.connect(self.ddot)
        self.signdel.clicked.connect(self.delete)

        signlist = [self.signadd, self.signmin, self.signmul, self.signdiv]
        for signbutt in signlist:
            signbutt.clicked.connect(self.modifysign)

        self.signequ.clicked.connect(self.equal)
        self.septhousand.stateChanged.connect(self.modifythousand)
        self.numdigits.currentIndexChanged.connect(self.moddig)

    def modifynum(self):
        numbutt = self.sender()
        self.value(numbutt.text())


    def modifysign(self):
        self.dflag = 0
        btn = self.sender()
        self.flag = btn.text()
        self.operate()

    def moddig(self):
        num = self.numdigits.currentIndex()
        self.num = int(num)
        current = self.disline.text()
        self.display(current)

    def ddot(self):
        self.dflag = 1
        current = self.disline.text()
        if '.' not in current:
            self.value('.')

    def equal(self):
        self.dflag = 0
        self.eq = 1
        self.operate()
        self.flag = '='
        if self.prevflag:
            self.stored = self.old if not self.old == None else self.stored
            self.stored = self.stored if not self.stored == None else self.new
        else:
            self.stored = self.new
        self.stored = str(float(self.stored)) + '00000'
        self.display(str(self.stored))
        self.new = None
        self.old = None
        self.eq = 0

    def value(self, info):
        if self.flag:
            current = '0'
            self.flag = ''
        else:
            current = self.disline.text()
            current = current.replace(',', '')

        try:
            pint, pdig = current.split('.')
            if len(pdig) < self.num:
                pdig += info
            current = '.'.join([pint, pdig])
        except:
            if self.num == 0 and self.dflag == 1:
                pass
            elif not int(current) == 0 or info == '.':
                current += info
            else:
                current = info
        self.display(current)

    def delete(self):
        self.dflag = 0
        self.stored = None
        self.display('0')

    def display(self, value):
        value = value.replace(',', '')
        self.new = value
        value = value[0:12] if '.' not in value else value[0:13]

        if self.thousand:
            try:
                pint, pdig = value.split('.')
                pint = pint[::-1]
                groups = re.findall(r'.{1,3}',pint)
                pint = ','.join(groups)
                pint = pint[::-1]
                value = '.'.join([pint, pdig])
            except:
                value = value[::-1]
                groups = re.findall(r'.{1,3}',value)
                value = ','.join(groups)
                value = value[::-1]

        if self.num == 0:
            out = re.search(r'([0-9,]*)',value)
            value = out.group(1)
        else:
            if '.' not in value:
                pass
            else:
                if self.num == 1:
                    out = re.findall(r'([0-9,]*)\.([0-9]{0,1})',value)
                    value = '.'.join(out[0])
                elif self.num == 2:
                    out = re.findall(r'([0-9,]*)\.([0-9]{0,2})',value)
                    value = '.'.join(out[0])
                elif self.num == 3:
                    out = re.findall(r'([0-9,]*)\.([0-9]{0,3})',value)
                    value = '.'.join(out[0])
                elif self.num == 4:
                    out = re.findall(r'([0-9,]*)\.([0-9]{0,4})',value)
                    value = '.'.join(out[0])
                else:
                    out = re.findall(r'([0-9,]*)\.([0-9]{0,5})',value)
                    value = '.'.join(out[0])
        self.disline.setText(value)

    def operate(self):
        try:
            if self.old == None:
                self.old = self.stored
            if self.prevflag == '+':
                temp = float(self.old) + float(self.new)
                self.old = self.old if temp >= 1e12 else temp
                self.display(str(self.old))

            elif self.prevflag == '-':
                temp = float(self.old) - float(self.new)
                self.old = self.old if temp >= 1e12 else temp
                self.display(str(self.old))

            elif self.prevflag == 'x':
                temp = float(self.old) * float(self.new)
                self.old = self.old if temp >= 1e12 else temp
                self.display(str(self.old))

            elif self.prevflag == '/':
                temp = float(self.old) / float(self.new)
                self.old = self.old if temp >= 1e12 else temp
                self.display(str(self.old))
            else:
                pass
        except:
            pass
        self.prevflag = self.flag
        if not self.eq:
            self.old = self.new

    def modifythousand(self):
        self.thousand = 1 if not self.thousand else 0
        current = self.disline.text()
        self.display(current)

currentApp = QApplication(sys.argv)
currentForm = simpleCalc()

currentForm.show()
currentApp.exec_()
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

        self.num0.clicked.connect(self.n0)
        self.num1.clicked.connect(self.n1)
        self.num2.clicked.connect(self.n2)
        self.num3.clicked.connect(self.n3)
        self.num4.clicked.connect(self.n4)
        self.num5.clicked.connect(self.n5)
        self.num6.clicked.connect(self.n6)
        self.num7.clicked.connect(self.n7)
        self.num8.clicked.connect(self.n8)
        self.num9.clicked.connect(self.n9)
        self.dot.clicked.connect(self.ddot)
        self.signdel.clicked.connect(self.delete)
        self.signadd.clicked.connect(self.addop)
        self.signmin.clicked.connect(self.minop)
        self.signmul.clicked.connect(self.mulop)
        self.signdiv.clicked.connect(self.divop)
        self.signequ.clicked.connect(self.equal)
        self.septhousand.stateChanged.connect(self.modifythousand)
        self.numdigits.currentIndexChanged.connect(self.moddig)

        # self.btnShow.clicked.connect(self.displayName)
        # self.chkItalic.stateChanged.connect(self.modifyItalic)

    def moddig(self):
        num = self.numdigits.currentIndex()
        self.num = int(num)
        current = self.disline.text()
        self.display(current)

    def n0(self):
        self.value('0')

    def n1(self):
        self.value('1')

    def n2(self):
        self.value('2')

    def n3(self):
        self.value('3')

    def n4(self):
        self.value('4')

    def n5(self):
        self.value('5')

    def n6(self):
        self.value('6')

    def n7(self):
        self.value('7')

    def n8(self):
        self.value('8')

    def n9(self):
        self.value('9')

    def ddot(self):
        self.dflag = 1
        current = self.disline.text()
        if '.' not in current:
            self.value('.')

    def addop(self):
        self.dflag = 0
        self.flag = '+'
        self.operate(self.flag)

    def mulop(self):
        self.dflag = 0
        self.flag = '*'
        self.operate(self.flag)

    def divop(self):
        self.dflag = 0
        self.flag = '/'
        self.operate(self.flag)

    def minop(self):
        self.dflag = 0
        self.flag = '-'
        self.operate(self.flag)

    def equal(self):
        self.dflag = 0
        self.eq = 1
        self.operate(self.prevflag)
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
        self.new = value.replace(',','')
        self.disline.setText(value)

    def operate(self, op):
        try:
            if self.prevflag == '+':
                temp = float(self.old) + float(self.new)
                self.old = self.old if temp >= 1e12 else temp
                self.display(str(self.old))

            elif self.prevflag == '-':
                temp = float(self.old) - float(self.new)
                self.old = self.old if temp >= 1e12 else temp
                self.display(str(self.old))

            elif self.prevflag == '*':
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

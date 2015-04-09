# __author__ = 'ee364b09'
# import re
#
# with open('target.xml', 'r') as f:
#     line = f.read()
# print(line)
# output = re.findall(r'<FirstName>\[(.*)\]</FirstName>', line)
# print(output)
# output = re.findall(r'<FirstName>\[(.*)\]</FirstName>\s*<LastName>\[(.*)\]</LastName>\s*<Address>\[(.*)\]</Address>\s*<City>\[(.*)\]</City>\s*<State>\[(.*)\]</State>\s*<ZIP>\[(.*)\]</ZIP>\s*<Email>\[(.*)\]</Email>', line)
# print(output)
# first, last, add, city, st, zip, email = output[0]
# print(email)

import sys

import re

from PySide.QtGui import *

from EntryForm import *

class EntryApplication(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(EntryApplication, self).__init__(parent)
        self.setupUi(self)

        self.btnClear.clicked.connect(self.clearmode)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnSave.clicked.connect(self.savemode)

        txtlist = [self.txtFirstName, self.txtLastName, self.txtAddress, self.txtCity, self.txtState, self.txtZip, self.txtEmail]
        for txt in txtlist:
            txt.textChanged.connect(self.writing)

        # self.txtFirstName.textChanged.connect(self.writing)
        # self.txtLastName.textChanged.connect(self.writing)
        # self.txtAddress.textChanged.connect(self.writing)
        # self.txtCity.textChanged.connect(self.writing)
        # self.txtState.textChanged.connect(self.writing)
        # self.txtZip.textChanged.connect(self.writing)
        # self.txtEmail.textChanged.connect(self.writing)

    def writing(self):
        self.btnLoad.setEnabled(False)
        self.btnSave.setEnabled(True)

    def wrong(self):
        self.btnSave.setEnabled(False)
        self.btnLoad.setEnabled(True)

    def clearmode(self):
        txtlist = [self.txtFirstName, self.txtLastName, self.txtAddress, self.txtCity, self.txtState, self.txtZip, self.txtEmail]
        for txt in txtlist:
            txt.setText('')

        # self.txtFirstName.setText('')
        # self.txtLastName.setText('')
        # self.txtAddress.setText('')
        # self.txtCity.setText('')
        # self.txtState.setText('')
        # self.txtZip.setText('')
        # self.txtEmail.setText('')
        # self.lblError.setText('')
        self.btnSave.setEnabled(False)
        self.btnLoad.setEnabled(True)

    def savemode(self):
        if self.txtFirstName.text() == '' or self.txtLastName.text() == '' or self.txtAddress.text() == '' or self.txtCity.text() == '':
            self.lblError.setText('Error: All entries must be populated!')
            self.wrong()
            return
        if self.txtState.text() not in self.states:
            self.lblError.setText('Error: State is not valid!')
            self.wrong()
            return

        try:
            value = int(self.txtZip.text())
            if value >= 10000 and value < 100000:
                pass
            else:
                self.lblError.setText('Error: ZIP is not valid!')
                self.wrong()
                return
        except:
            self.lblError.setText('Error: ZIP is not valid!')
            self.wrong()
            return

        output = re.search(r'\w+@\w+\.\w+',self.txtEmail.text())
        if not output:
            self.lblError.setText('Error: Email is not valid!')
            self.wrong()
            return
        self.lblError.setText('')
        self.saveXML()

    def saveXML(self):
        output = '<?xml version="1.0" encoding="UTF-8"?>\n<user>\n'
        output += '	<FirstName>{}</FirstName>\n'.format(self.txtFirstName.text())
        output += '	<LastName>{}</LastName>\n'.format(self.txtLastName.text())
        output += '	<Address>{}</Address>\n'.format(self.txtAddress.text())
        output += '	<City>{}</City>\n'.format(self.txtCity.text())
        output += '	<State>{}</State>\n'.format(self.txtState.text())
        output += '	<ZIP>{}</ZIP>\n'.format(self.txtZip.text())
        output += '	<Email>{}</Email>\n'.format(self.txtEmail.text())
        output += '</user>'
        fout = open('target.xml', 'w')
        fout.write(output)
        fout.close()


    def loadFromXmlFile(self, filePath):
        """
        Handling the loading of the data from the given file name. This method should only be  invoked by the
        'loadData' method.
        """
        with open(filePath, 'r') as f:
            line = f.read()
        output = re.findall(r'<FirstName>(.*)</FirstName>\s*<LastName>(.*)</LastName>\s*<Address>(.*)</Address>\s*<City>(.*)</City>\s*<State>(.*)</State>\s*<ZIP>(.*)</ZIP>\s*<Email>(.*)</Email>', line)
        first, last, add, city, st, zip, email = output[0]
        self.txtFirstName.setText(first)
        self.txtLastName.setText(last)
        self.txtAddress.setText(add)
        self.txtCity.setText(city)
        self.txtState.setText(st)
        self.txtZip.setText(zip)
        self.txtEmail.setText(email)
        self.lblError.setText('')
        self.btnSave.setEnabled(True)
        self.btnLoad.setEnabled(False)

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return
        self.loadFromXmlFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = EntryApplication()

    currentForm.show()
    currentApp.exec_()

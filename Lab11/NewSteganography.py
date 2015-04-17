#! /usr/local/bin/python3.4
__author__ = "Xihui Wang"

from Steganography import *
import re


class NewSteganography(Steganography):

    def wipeMedium(self):
        out = Image.open(self.imagePath)
        l, h = out.size
        pix = list(out.getdata())

        if self.direction == 'horizontal':
            for i in range(len(pix)):
                ele_bv = bin(pix[i])[2:]
                ele_bv = ele_bv[:-1] + '0'
                pix[i] = int(ele_bv, 2)
        else:
            for i in range(int(l)):
                for j in range(int(h)):
                    ele_bv = bin(pix[j*int(l) + i])[2:]
                    ele_bv = ele_bv[:-1] + '0'
                    pix[j*int(l) + i] = int(ele_bv, 2)
        img = Image.fromstring('L', (int(l), int(h)), bytes(pix))
        img.save(self.imagePath)
        return

    def checkIfMessageExists(self):
        result = self.extractMessageFromMedium()
        if result is None:
            return False, None
        else:
            ttype = re.findall(r'<message type="(.*?)"', result.XmlString)
            return True, ttype[0]

if __name__ == "__main__":
    imagePath = 'xx.png'
    stegan = NewSteganography(imagePath, 'horizontal')
    res = stegan.checkIfMessageExists()
    print(res)

    stegan.wipeMedium()

    xstegan = NewSteganography('wiped.png', 'horizontal')
    res = xstegan.checkIfMessageExists()
    print(res)

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
        # result = self.extractMessageFromMedium()
        # if result is None:
        #     return False, None
        # else:
        #     ttype = re.findall(r'<message type="(.*?)"', result.XmlString)
        #     return True, ttype[0]

        out = Image.open(self.imagePath)
        l, h = out.size
        pix = list(out.getdata())
        messg = ''
        lim = 70 * 8
        ind = 0

        if self.direction == 'horizontal':
            for ele in pix:
                ind += 1
                ele_bv = bin(ele)[2:]
                # ele_bv = str(BitVector.BitVector(intVal=ele))
                messg += ele_bv[-1]
                if ind == lim:
                    break
        else:
            for i in range(int(l)):
                for j in range(int(h)):
                    ind += 0
                    ele_bv = bin(pix[j*int(l) + i])[2:]
                    # ele_bv = str(BitVector.BitVector(intVal=pix[j*int(l) + i]))
                    messg += ele_bv[-1]
                    if ind == lim:
                        break

        temp = [chr(int(messg[8*times: 8*(times+1)], 2)) for times in range(int(len(messg)/8))]
        messgstr = ''.join(temp)
        out = re.findall(r'<\?xml version="1\.0" encoding="UTF-8"\?>\n<message type="(.*?)"', messgstr)
        if not out:
            return False, None
        else:
            return True, out[0]

if __name__ == "__main__":
    imagePath = 'nature_sunflower_h.png'
    stegan = NewSteganography(imagePath, 'horizontal')
    _, res = stegan.checkIfMessageExists()
    print(res)

    # stegan.wipeMedium()
    #
    # xstegan = NewSteganography('horizontal')
    # res = xstegan.checkIfMessageExists()
    # print(res)

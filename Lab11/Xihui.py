#! /usr/local/bin/python3.4
__author__ = "Xihui Wang"

import base64
import re
from PIL import Image
import BitVector
# --allow-external BitVector --allow-unverified BitVector


class Message:
    # initialize all the variables, and  check if all inputs are valid
    def __init__(self, **kwargs):
        if len(kwargs) == 1:
            try:
                self.XmlString = kwargs['XmlString']
            except:
                raise ValueError('missing argument of message')
            
        elif len(kwargs) == 2:
            try:
                self.filePath = kwargs['filePath']
                self.messageType = kwargs['messageType']
                if not self.filePath:
                    raise ValueError('file path should not be none')
                if self.messageType != 'Text' and self.messageType != 'GrayImage' and self.messageType != 'ColorImage':
                    raise ValueError('type of self.messageType is wrong')
            except:
                raise ValueError('missing argument of message')

        else:
            raise ValueError('missing argument of message')

    # return the size of the message, raise exception if nothing inside the message
    def getMessageSize(self):
        if len(self.XmlString) == 0:
            raise Exception
        return len(self.XmlString)

    # save the message back to image, and there are two types of image. one is color, the other one is gray
    def saveToImage(self, targetImagePath):
        if not self.XmlString:
            raise Exception
        output = re.findall(r'<message type="(.*)" size="(.*),(.*)" encrypted=".*">\n(.*)\n</message>', self.XmlString)
        if not output:
            raise TypeError('wrong XmlString')
        mtype, l, h, message = output[0]
        # this will return a list of numbers that represent the image file
        result = list(base64.b64decode(message))

        if mtype == 'GrayImage':
            img = Image.fromstring('L', (int(l), int(h)), bytes(result))
            # img.show()
        elif mtype == 'ColorImage':
            # since the color image will contains a pix of tuple, and inside the tuple are the rgb infos, we need to divide it into three parts and combine them into one.
            ind = int(len(result)/3)
            img1 = Image.fromstring('L', (int(l), int(h)), bytes(result[0: ind]))
            img2 = Image.fromstring('L', (int(l), int(h)), bytes(result[ind: ind * 2]))
            img3 = Image.fromstring('L', (int(l), int(h)), bytes(result[ind * 2: ind * 3]))
            img = Image.merge('RGB', (img1, img2, img3))
            # img.show()
        else:
            raise TypeError
        
        img.save(targetImagePath)

    # decode the message and save back to text file
    def saveToTextFile(self, targetTextFilePath):
        if not self.XmlString:
            raise Exception
        output = re.findall(r'<message type="(.*)" size=".*" encrypted=".*">\n(.*)\n</message>', self.XmlString)
        mtype, message = output[0]
        if mtype != 'Text':
            raise TypeError
        result = str(base64.b64decode(message), 'utf-8')

        fout = open(targetTextFilePath, 'w')
        fout.write(result)
        fout.close()

    # save the target message into image or text file
    def saveToTarget(self, targetPath):
        try:
            self.saveToImage(targetPath)
        except:
            self.saveToTextFile(targetPath)

    # get the xmlstring from the text file or image file
    def getXmlString(self):
        if self.messageType == 'GrayImage':
            out = Image.open(self.filePath)
            l,h = out.size
            pix = list(out.getdata())
            output = base64.b64encode(bytes(pix))
            return '<?xml version="1.0" encoding="UTF-8"?>\n<message type="{}" size="{},{}" encrypted="{}">\n{}\n</message>'.format(self.messageType, l, h, 'False', str(output)[2:-1])

        elif self.messageType == 'ColorImage':
            out = Image.open(self.filePath)
            l, h = out.size
            pix = list(out.getdata())
            arr1, arr2, arr3 = [], [], []
            for ele in pix:
                x, y, z = ele
                arr1 += [x]
                arr2 += [y]
                arr3 += [z]
            arr = arr1 + arr2 + arr3
            output = base64.b64encode(bytes(arr))
            return '<?xml version="1.0" encoding="UTF-8"?>\n<message type="{}" size="{},{}" encrypted="{}">\n{}\n</message>'.format(self.messageType, l, h, 'False', str(output)[2:-1])

        elif self.messageType == 'Text':
            with open(self.filePath, 'rt') as f:
                line = f.read()
            output = base64.b64encode(line.encode('ascii'))
            return '<?xml version="1.0" encoding="UTF-8"?>\n<message type="{}" size="{}" encrypted="{}">\n{}\n</message>'.format(self.messageType, len(line), 'False', str(output)[2:-1])
        else:
            raise TypeError

class Steganography:
    # initialize all the variables, and  check if all inputs are valid
    def __init__(self, imagePath, direction='horizontal'):
        if direction != 'horizontal' and direction != 'vertical':
            raise ValueError('direction can only be hor or ver')
        try:
            img = Image.open(imagePath)
            pix = list(img.getdata())
            if type(pix[0]) != int:
                raise TypeError('the image loaded should be gray image')
        except:
            raise TypeError('the image loaded should be gray image')
        self.direction = direction
        self.imagePath = imagePath

    # embed the message into the given medium. for this case, the medium should be gray image
    # there are two way to embed the message, one is horizontal, and the other one is vertical
    def embedMessageInMedium(self, message, targetImagePath):
        if not isinstance(message, Message):
            raise TypeError('message should be Message type')

        xml = message.getXmlString()
        xml_bv = list(BitVector.BitVector(textstring=xml))

        out = Image.open(self.imagePath)
        l, h = out.size
        pix = list(out.getdata())
        if len(pix) < len(xml_bv):
            raise ValueError('the message is too large')

        if self.direction == 'horizontal':
            for i in range(len(xml_bv)):
                ele_bv = str(BitVector.BitVector(intVal=pix[i]))
                ele_bv = ele_bv[:-1] + str(xml_bv[i])
                pix[i] = int(ele_bv, 2)
            img = Image.fromstring('L', (int(l), int(h)), bytes(pix))
            img.save(targetImagePath)
            return
        else:
            ind = 0
            for i in range(int(l)):
                for j in range(int(h)):
                    ele_bv = str(BitVector.BitVector(intVal=pix[j*int(l) + i]))
                    ele_bv = ele_bv[:-1] + str(xml_bv[ind])
                    pix[j*int(l) + i] = int(ele_bv, 2)
                    ind += 1
                    if ind == len(xml_bv):
                        img = Image.fromstring('L', (int(l), int(h)), bytes(pix))
                        img.save(targetImagePath)
                        return

    # extract the message from the given gray medium
    # two ways to get the message back, one is horizontal, the other is vertical
    # also if nothing embedded in the medium, return none
    def extractMessageFromMedium(self):
        out = Image.open(self.imagePath)
        l, h = out.size
        pix = list(out.getdata())
        messg = ''

        if self.direction == 'horizontal':
            for ele in pix:
                ele_bv = str(BitVector.BitVector(intVal=ele))
                messg += ele_bv[-1]
        else:
            for i in range(int(l)):
                for j in range(int(h)):
                    ele_bv = str(BitVector.BitVector(intVal=pix[j*int(l) + i]))
                    messg += ele_bv[-1]
                    
        temp = [chr(int(messg[8*times: 8*(times+1)], 2)) for times in range(int(len(messg)/8))]
        messgstr = ''.join(temp)
        out = re.findall(r'<\?xml version="1\.0" encoding="UTF-8"\?>\n<message type=".*" size=".*" encrypted=".*">\n.*\n</message>', messgstr)
        if not out:
            return None
        else:
            return Message(XmlString=out[0])
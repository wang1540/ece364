__author__ = 'ee364b09'
import os
import uuid
import unittest
from PIL import Image
from Steganography import *
import base64

if __name__ == "__main__":
    # test----save to text file
    # sourcePath = 'full.xml'
    # message = Message(filePath=sourcePath, messageType='Text')
    # with open(message.filePath, 'rt') as f:
    #     line = f.read()
    # message.XmlString = line
    # message.saveToTarget('aa')

    # test----save to image file
    # part1----Gray
    # sourcePath = 'dog.xml'
    # message = Message(filePath=sourcePath, messageType='GrayImage')
    # with open(message.filePath, 'rt') as f:
    #     line = f.read()
    # message.XmlString = line
    # message.saveToTarget('qq.png')
    # part2----Color
    # sourcePath = 'sunflower.xml'
    # message = Message(filePath=sourcePath, messageType='ColorImage')
    # with open(message.filePath, 'rt') as f:
    #     line = f.read()
    # message.XmlString = line
    # message.saveToTarget('xx.png')

    # sourcePath = 'full.txt'
    # message = Message(filePath=sourcePath, messageType='Text')

    # sourcePath = 'dog.png'
    # message = Message(filePath=sourcePath, messageType='GrayImage')

    # sourcePath = 'sunflower.png'
    # message = Message(filePath=sourcePath, messageType='ColorImage')

    # test----getXmlString
    # f = open('aa.xml','w')
    # f.write(message.getXmlString())
    # f.close()



    # test----embed
    # embed full.txt into lena.png. xx.png is output that contains message.
    # AND compare the getXmlString of the xx.png and lena.png we could conclude that the two are different
    #
    # sourcePath = 'full.txt'
    # message = Message(filePath=sourcePath, messageType='Text')
    # imagePath = 'lena.png'
    # stegan = Steganography(imagePath, 'vertical')
    #
    # stegan.embedMessageInMedium(message, 'xx.png')
    #
    # sourcePath1 = 'lena.png'
    # message1 = Message(filePath=sourcePath1, messageType='GrayImage')
    # f = open('aa.xml','w')
    # f.write(message1.getXmlString())
    # f.close()
    #
    # sourcePath2 = 'xx.png'
    # message2 = Message(filePath=sourcePath2, messageType='GrayImage')
    # f = open('bb.xml','w')
    # f.write(message2.getXmlString())
    # f.close()

    # sourcePath = 'full.txt'
    # message = Message(filePath=sourcePath, messageType='Text')
    # imagePath = 'lena.png'
    # stegan = Steganography(imagePath, 'horizontal')
    #
    # stegan.embedMessageInMedium(message, 'xx.png')
    # mess = stegan.extractMessageFromMedium()
    # print(mess)





    # sourcePath = '/home/ecegrid/a/ee364b09/Lab11/t&h/tan.txt'
    # message = Message(filePath=sourcePath, messageType='Text')
    # imagePath = '/home/ecegrid/a/ee364b09/Lab11/t&h/IMG_2645.png'
    # stegan = Steganography(imagePath, 'vertical')
    # stegan.embedMessageInMedium(message, '/home/ecegrid/a/ee364b09/Lab11/t&h/tan_txt_v.png')

    # sourcePath = '/home/ecegrid/a/ee364b09/Lab11/t&h/IMG_2648.png'
    # message = Message(filePath=sourcePath, messageType='ColorImage')
    # imagePath = '/home/ecegrid/a/ee364b09/Lab11/t&h/IMG_2645.png'
    # stegan = Steganography(imagePath, 'horizontal')
    # stegan.embedMessageInMedium(message, '/home/ecegrid/a/ee364b09/Lab11/t&h/tan_hui_h.png')

    # sourcePath = '/home/ecegrid/a/ee364b09/Lab11/t&h/IMG_2645(1).png'
    # message = Message(filePath=sourcePath, messageType='ColorImage')
    # imagePath = '/home/ecegrid/a/ee364b09/Lab11/t&h/IMG_2646.png'
    # stegan = Steganography(imagePath, 'horizontal')
    # stegan.embedMessageInMedium(message, '/home/ecegrid/a/ee364b09/Lab11/t&h/xinba_tan_h.png')

    sourcePath = '/home/ecegrid/a/ee364b09/Lab11/t&h/IMG_2645(1).png'
    message = Message(filePath=sourcePath, messageType='ColorImage')
    imagePath = '/home/ecegrid/a/ee364b09/Lab11/t&h/IMG_2649.png'
    stegan = Steganography(imagePath, 'vertical')
    stegan.embedMessageInMedium(message, '/home/ecegrid/a/ee364b09/Lab11/t&h/hui_tan_v.png')

    # sourcePath = '/home/ecegrid/a/ee364b09/Lab11/t&h/IMG_2649(1).png'
    # message = Message(filePath=sourcePath, messageType='ColorImage')
    # imagePath = '/home/ecegrid/a/ee364b09/Lab11/t&h/IMG_2645.png'
    # stegan = Steganography(imagePath, 'vertical')
    # stegan.embedMessageInMedium(message, '/home/ecegrid/a/ee364b09/Lab11/t&h/hui_tan_v.png')

    out = Image.open(imagePath)
    l, h = out.size
    print('{} and {}'.format(l, h))
    pix1 = list(out.getdata())
    out = Image.open(sourcePath)
    l, h = out.size
    print('{} and {}'.format(l, h))
    pix2 = list(out.getdata())
    print(len(pix1))
    print(len(pix2))

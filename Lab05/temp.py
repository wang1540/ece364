#! /usr/bin/env python3.4
from pprint import pprint as pp

def getDirectory():
    map={}
    with open ('Phone Directory.txt','r') as f:
        wholelines = f.readlines()
    for lines in wholelines:
        fir, mid, last, num1, num2 = lines.split()
        number = num1 + " " + num2
        T = fir, mid, last
        map[T] = number
    return map

def getPhoneByPartialName (partialname):
    map = getDirectory()
    numlist = []
    for T in map.keys():
        fir,_,last = T
        if partialname == fir:
            numlist += [map[T]]
        if partialname == last:
            numlist += [map[T]]
    return numlist

def reverseLookup (areaCode):
    map = getDirectory()
    namelist =[]
    for T in map.keys():
        code = map[T][1:4]
        if code == areaCode:
            namelist += [T]
    return namelist

if __name__ == "__main__":
    map = getDirectory()
    #pp(map)
    listn = getPhoneByPartialName('Gloria')
    print (listn)
    nlist = reverseLookup('510')
    print (nlist)
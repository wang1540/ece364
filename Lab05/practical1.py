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
        if partialname == fir or partialname == last:
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

def getLargestProduct():
    with open ('Number Grid.txt','r') as f:
        wholelines = f.readlines()

    for i in range(len(wholelines)):
        wholelines[i] = wholelines[i].split()

    prod = 0
    for i in range(len(wholelines)):
        row = wholelines[i]
        Temp = getLargestPartition(row,4)
        #print (Temp)
        if prod < Temp[1]:
            prod = Temp[1]
            maxlist = Temp[0]
            direction = 'H'
    # print (prod)
    # print (maxlist)
    for i in range(len(wholelines)):
        col = []
        for j in range(20):
            col = col + [wholelines[j][i]]
        Temp = getLargestPartition(col,4)
        if prod < Temp[1]:
            prod = Temp[1]
            maxlist = Temp[0]
            direction = 'V'

    T = maxlist, prod, direction
    #return tuple
    return T

def getListProduct(numList):
    result = 1
    if numList == []:
        return 0
    else:
        for i in numList:
            result = int(i) * result
        return result

def partitition(numList, n):
    total_round = len(numList) - n + 1
    p = []
    for i in range(total_round):
        p += [numList[i:i+n]]
    return p

def getLargestPartition(numList, n):
    p = partitition(numList, n)
    prod = 0
    for sublist in p:
        temp = getListProduct(sublist)
        if prod < temp:
            prod = temp
            T = sublist, prod
    return T

if __name__ == "__main__":
    print (getLargestProduct())
    # print (getListProduct([1,2,3]))
    # print (partitition([2,1,4,3],2))
    # print (getLargestPartition([2,1,4,3],2))

    map = getDirectory()
    #pp(map)
    listn = getPhoneByPartialName('Gloria')
    print (listn)
    nlist = reverseLookup('510')
    print (nlist)
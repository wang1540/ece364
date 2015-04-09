#! /usr/bin/env python3.4

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
            llist = sublist
    T = llist, prod
    return T

if __name__ == "__main__":
    temp = ['49', '49', '99', '40', '17', '81', '18', '57', '60', '87', '17', '40', '98', '43', '69', '48', '04', '56', '62', '00']
    print (getLargestProduct())
    print (getListProduct(['5','2','3']))
    print (partitition(temp,4))
    print (getLargestPartition(temp,4))


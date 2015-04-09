#! /usr/bin/env python3.4

import glob
from pprint import pprint as pp

def getWordFrequency():
    filelist = glob.glob('files/*.txt')
    ww = []
    for files in filelist:
        with open(files, 'r') as f:
            temp = f.readlines()
        temp = str(temp[0])
        temp = temp.replace(",","").replace(".","").replace("!","").replace("?","").split()
        ww = ww + temp
    Map={}
    for key in ww:
        if key in Map.keys():
            Map[key]=Map[key]+1
        else:
            Map[key]=1
    #pp(Map)
    return Map

def getDuplicates():
    group = {}
    map = {}
    filelist = glob.glob('files/*.txt')

    for files in filelist:
        with open(files, 'r') as f:
            temp = str(f.readlines()[0])
        if not temp in map.keys():
            tt = temp.replace(",","").replace(".","").replace("!","").replace("?","").split()
            wordCount = len(set(tt))
            map[temp] = [wordCount] + [[files[:-4][6:]]]
        else:
            map[temp][1] = map[temp][1] + [files[:-4][6:]]

    for haha in map.keys():
        wordCount, groupList = map[haha]
        group[groupList[0]]= wordCount,groupList
    #pp(group)
    return group

def getPurchaseReport():
    filelist = glob.glob('purchases/purchase_*.txt')
    pricetable={}

    with open('purchases/Item List.txt', 'r') as f:
        itemlist = f.readlines()
    for l in itemlist[2:]:
        itemm, pricee = l.split()
        pricee = pricee.replace("$","")
        pricetable[itemm] = pricee

    report={}
    for file in filelist:
        summ = 0
        with open(file,'r') as f:
            lines = f.readlines()
        for l in lines[2:]:
            item, quan = l.split()
            if item in pricetable.keys():
                summ = summ + float(pricetable[item]) * int(quan)
        report[int(file[:-4][19:])] = round(summ,2)
    #pp(report)
    return report

def getTotalSold():
    soldlist={}
    filelist = glob.glob('purchases/purchase_*.txt')
    for file in filelist:
        with open(file,'r') as f:
            lines = f.readlines()
        for l in lines[2:]:
            items, quan = l.split()
            if not items in soldlist.keys():
                soldlist[items] = int(quan)
            else:
                soldlist[items] = soldlist[items] + int(quan)
    #pp(soldlist)
    return soldlist

if __name__ == "__main__":
    getWordFrequency()
    getDuplicates()
    getPurchaseReport()
    getTotalSold()
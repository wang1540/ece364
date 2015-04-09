#! /usr/bin/env python3.4

import glob
import re
import os
from pprint import pprint as pp

def getWordFrequency(word):
    Map={}
    for j in range(len(ww)):
        key=ww[j]
        if key in Map.keys():
            Map[key]=Map[key]+1
        else:
            Map[key]=1
    #pp(Map)
    return Map

def getDuplicates():
    group={}
    for haha in map.keys():
        wordCount=map[haha][0]
        groupList=map[haha][1]
        kkey=groupList[0]
        T=(wordCount,groupList)
        group[kkey]=T
    #pp(group)
    return group

def getPurchaseReport():
    report={}
    for file in fu:
        with open(file,'r') as f:
            i=0
            summ=0
            for l in f:
                i=i+1
                if (i>2):
                    item=l.split()[0]
                    if item in pricetable.keys():
                        num=l.split()[1]
                        summ=summ + float(pricetable[item]) * int(num)
            report[int(file[53:][:-4])]=round(summ,2)
    #pp(report)
    return report

def getTotalSold():
    soldlist={}
    for file in fu:
        with open(file,'r') as f:
            i=0
            for l in f:
                i=i+1
                if (i>2):
                    items=l.split()[0]
                    if not items in soldlist.keys():
                        soldlist[items]=int(l.split()[1])
                    else:
                        soldlist[items]=soldlist[items]+int(l.split()[1])
    #pp(soldlist)
    return soldlist

if __name__ == "__main__":
    filelist=glob.glob(os.path.dirname(os.path.abspath(__file__))+'/files/*.txt')
    ww=[]
    map={}
    for i in range(len(filelist)):
        with open(filelist[i],'r') as f:
            for l in f:
                temp=re.findall(r"[\w']+", l)
                ww=ww+temp
                if not l in map.keys():
                    wordCount=len(set(temp))
                    value=[wordCount]+[[filelist[i][40:][:-4]]]
                    map[l]=value
                else:
                    map[l][1]=map[l][1]+[filelist[i][40:][:-4]]
    getWordFrequency('mauris')
    getDuplicates()

    fu=glob.glob(os.path.dirname(os.path.abspath(__file__))+'/purchases/purchase_*.txt')
    pricefile=os.path.dirname(os.path.abspath(__file__))+'/purchases/Item List.txt'
    pricetable={}
    with open(pricefile,'r') as f:
        i=0
        for l in f:
            i=i+1
            if (i>2):
                price=l.split()
                price[1]=price[1][1:]
                pricetable[price[0]]=price[1]
    getPurchaseReport()
    getTotalSold()

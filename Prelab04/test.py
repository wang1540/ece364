#! /usr/bin/env python3.4

import glob
import re
import os
from pprint import pprint as pp

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
            #print (int(file[53:][:-4]))
            #print (sum)
            report[int(file[53:][:-4])]=round(summ,2)
    pp(report)
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
    pp(soldlist)
    return soldlist


if __name__ == "__main__":
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
    report = getPurchaseReport()
    soldlist = getTotalSold()
#! /usr/bin/env python3.4
import glob
import os
from pprint import pprint as pp

def generateReportForAllViruses():
    reportv={}
    for file in filelist:
        cnt=0
        vunit=0
        vcost=0
        with open(file,'r') as f:
            for l in f:
                if cnt > 3:
                    l=l.split()
                    vname = l[1]
                    unit = l[2]
                    cost = l[3][1:]
                    if vname in reportv.keys():
                        vunit=int(unit) + reportv[vname][0]
                        vcost=float(cost) + reportv[vname][1]
                        T=(vunit,round(vcost,2))
                        reportv[vname] = T
                    else:
                        vunit=int(unit)
                        vcost=float(cost)
                        T=(vunit,round(vcost,2))
                        reportv[vname] = T
                cnt = cnt +1
    pp(reportv)
    return reportv

def generateReportForAllUsers():
    reportuser={}
    for i in range(len(filelist)):
        cnt=0
        sunit=0
        scost=0
        with open(filelist[i],'r') as f:
            for l in f:
                if cnt == 0:
                    uid = l[9:][:-1]
                    name = map[uid]
                    #print (name)
                    if name in reportuser.keys():
                        sunit=reportuser[name][0]
                        scost=reportuser[name][1]
                if cnt > 3:
                    l=l.split()
                    unit = l[2]
                    cost = l[3][1:]
                    #print (cost)
                    sunit = int(unit) + sunit
                    scost = scost + float(cost)
                cnt = cnt +1
        T=(sunit,round(scost,2))
        reportuser[name]=T
    #pp(reportuser)
    return reportuser

def getUsersWithoutREports():
    noset=set()
    test = map

    for i in filelist:
        cnt = 0
        with open(i,'r') as f:
            for l in f:
                if cnt == 0:
                    uid = l[9:][:-1]
                    if uid in test.keys():
                        test.pop(uid)

    for key in test.values():
        noset.add(key)
    #print (len(noset))
    return (noset)

def getTotalSpending():
    scost=0
    for i in filelist:
        cnt=0
        with open (i,'r') as f:
            for l in f:
                if cnt > 3:
                    l=l.split()
                    cost = l[3][1:]
                    scost = scost + float(cost)
                cnt = cnt +1
    scost=round(scost,2)
    #print (scost)
    return scost

if __name__ == "__main__":
    filelist = glob.glob(os.path.dirname(os.path.abspath(__file__))+'/reports/*.txt')
    #userlist=[]
    #Id=[]
    map={}
    cnt=0
    with open ("users.txt",'r') as f:
        for l in f:
            cnt=cnt+1
            if cnt > 2:
                l=l.split("|")
                Id=l[1].strip()
                temp=l[0].split(",")
                u=temp[1].strip()+" "+temp[0].strip()
                map[Id]=u
    #pp(map)
    #print (len(map))

    generateReportForAllUsers()
    generateReportForAllViruses()
    getUsersWithoutREports()
    getTotalSpending()

    print("done")

"""
    for file in filelist:
        with open(file,'r') as f:
            cnt=0
            for l in f:
                if cnt > 3:
                    print (l)
                cnt=cnt+1
"""
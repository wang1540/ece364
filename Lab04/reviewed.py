#! /usr/bin/env python3.4
import glob
import os
from pprint import pprint as pp

def generateReportForAllViruses():

    filelist = glob.glob('reports/*.txt')
    virusDictionary = {}

    for filePath in filelist:
        with open(filePath, "r") as rFile:
            lines = rFile.readlines()[4:]

        for line in lines:
            _, virus, units, cost = line.split()
            units = int(units)
            cost = float(cost.replace("$", ""))

            if virus in virusDictionary.keys():
                currentUnits, currentCost = virusDictionary[virus]
                units, cost = units + currentUnits, round(cost + currentCost,2)

            virusDictionary[virus] = units, cost
    return reportv

def generateReportForAllUsers():
    filelist = glob.glob('reports/*.txt')
    reportuser={}
    map = base()
    for i in range(len(filelist)):
        cnt = 0
        sunit = 0
        scost = 0
        with open(filelist[0], 'r') as f:
            lines = f.readlines()
        userid = lines[0].split()[2]
        name = map[userid]

        for reportline in lines[4:]:


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
    filelist = glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/reports/*.txt')
    noset=set()
    test = base()

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
    filelist = glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/reports/*.txt')
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


def base():
    filelist = glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/reports/*.txt')
    # userlist=[]
    #Id=[]
    map = {}
    cnt = 0
    with open("users.txt", 'r') as f:
        for l in f:
            cnt = cnt + 1
            if cnt > 2:
                l = l.split("|")
                Id = l[1].strip()
                temp = l[0].split(",")
                u = temp[1].strip() + " " + temp[0].strip()
                map[Id] = u
    #pp(map)
    #print (len(map))
    return map,filelist



if __name__ == "__main__":

    base()
    generateReportForAllUsers()
    generateReportForAllViruses()
    getUsersWithoutREports()
    getTotalSpending()

    print("done")

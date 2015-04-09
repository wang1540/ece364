#! /usr/bin/env python3.4

import glob
from pprint import pprint as pp

def getWordFrequency():

    filelist = glob.glob('files/*.txt')

    # (AG): Use more descriptive variable names, as you do in many places.
    ww = []
    for files in filelist:
        with open(files, 'r') as f:
            temp = f.readlines()
        # (AG): Why did you cast this to a string? When you read a file, it is already a string.
        temp = str(temp[0])
        temp = temp.replace(",","").replace(".","").replace("!","").replace("?","").split()
        ww = ww + temp
    # (AG): Use spaces in assignments and between lines, or I will have a heart-attack.
    Map = {}
    for key in ww:
        if key in Map.keys():
            # (AG): While this would work here, it might cause problems in other scenarios, as we will
            # see later in the semester. It is better to read the content, modify it, then assign it again.
            Map[key]=Map[key]+1
        else:
            Map[key]=1
    # (AG): Instead of using pp here, and disabling it when you submit, use it in the conditional main block
    # and then you don't have to disable it.
    #pp(Map)
    return Map

def getDuplicates():
    group = {}
    map = {}
    filelist = glob.glob('files/*.txt')

    # (AG): The variable "files" should be singular to avoid confusion.
    for files in filelist:
        with open(files, 'r') as f:
            temp = str(f.readlines()[0])
        if not temp in map.keys():
            tt = temp.replace(",","").replace(".","").replace("!","").replace("?","").split()
            wordCount = len(set(tt))
            # (AG): YOu are trying to extract the file name by extracting a specific substring. This would
            # work for this exercise, but it is a bad idea in general. Look into the functionality of the
            # module "os": os.path.basename and os.path.splitext
            map[temp] = [wordCount] + [[files[:-4][6:]]]
        else:
            map[temp][1] = map[temp][1] + [files[:-4][6:]]
    # (AG): Seriously?! This is your choice of a variable name? haha?
    for haha in map.keys():
        wordCount, groupList = map[haha]
        group[groupList[0]]= wordCount,groupList
    #pp(group)
    return group

def getPurchaseReport():
    # (AG): Good job! Aside for the comment I mentioned earlier, this is a great implementation. It is
    # succinct and readable at the same time. Hopefully, you can write code like this for the rest of the semester.
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
    # (AG): Again, good job on this one, too! If you fix the spaces, and the variable names, you will end up
    # with code like mine.
    soldlist = {}
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

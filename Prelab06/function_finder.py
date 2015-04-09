#! /usr/bin/env python3.4
import re
import sys
import os.path

def printout(fun, vals):
    print(fun)
    vlist = vals.split(',')
    for i in range(len(vlist)):
        print("Arg{}: {}".format(i+1,vlist[i].strip()))

def matchfunction(filename):
    with open(filename,'r') as f:
        lines = f.readlines()

    for line in lines:
        out = re.search(r'def\s([a-z\w\_]*)\s*\(([\w,\s=]*)\)\:',line)
        if out:
            print(out.group())
            functionname = out.group(1)
            vals = out.group(2)
            printout(functionname,vals)

def main_test():
    inputfile = 'module1.py'
    if os.path.isfile(inputfile) == False:
        print("Error: Could not read {}".format(inputfile))
        return
    matchfunction(inputfile)

def main():
    if len(sys.argv) == 2:
        inputFileName = sys.argv[1]
        if os.path.isfile(inputFileName) == False:
            print("Error: Could not read {}".format(inputFileName))
            return
        matchfunction(inputFileName)

    else:
        print("Usage: function_finder.py [python_file_name]")

if __name__ == "__main__":
    #main()
    #for test purpose:
    main_test()
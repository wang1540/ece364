#! /usr/bin/env python3.4
import re

def convertToAttrib():

    with open("points.xml") as f:
        lines = f.read()
    output = "points_out.xml"
    fout = open(output,'w')
    fout.write('<?xml version="1.0"?>\n<coordinates>\n')
    idd = re.findall(r"<ID>(.*?)</ID>",lines)
    x_total = re.findall(r"<X>(.*?)</X>",lines, re.DOTALL)
    y = re.findall(r"<Y>(.*?)</Y>",lines)
    x = []
    for i in x_total:
        x += i.split()
    for i in range(len(idd)):
        fout.write('   <point ID="'+idd[i]+'"'+' X="'+x[i]+'"' + ' Y="' + y[i] + '"' + ' />\n')
    fout.write('</coordinates>')
    fout.close

if __name__ == "__main__":

    convertToAttrib()
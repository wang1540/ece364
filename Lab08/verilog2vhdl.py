#! /usr/local/bin/python3.4
__author__ = "Xihui Wang"
import sys
from vtools import *

def main(infile, outfile=""):

        lines = []

        try:
            with open(infile, 'r') as fin:
                lines = fin.readlines()

        except IOError as r:
            print('Error:', r)
            exit(2)

        output = []

        for line in lines:
            try:
                name1, name2, T = parse_net(line)
                outputList = ["{0}=>{1}".format(fst, snd) for fst, snd in T]
                elementsString = ", ".join(outputList)
                outputLine = "{0}: {1} PORT MAP({2});".format(name2, name1, elementsString)
                output.append(outputLine)

            except ValueError as e:
                print('Error input file is not a valid verilog port map!')
                print('Error:', e)
                exit(4)
        finalString = "\n".join(output)

        if not outfile:
            print(finalString)
            exit(0)

        try:
            with open(outfile, 'w') as fout:
                fout.write(finalString)

        except IOError as r:
            print('Error:', r)
            exit(3)

if __name__ == "__main__":

    if len(sys.argv) > 3:
        print("Usage: verilog2vhdl.py [infile] [outfile]")
        exit(1)

    if len(sys.argv) == 1:

        for name in sys.stdin:
            try:
                with open(name[:-1], 'r') as fin:
                    lines = fin.readlines()
            except IOError as r:
                print('Error:', r)
                exit(2)

    elif len(sys.argv) == 2:
        main(sys.argv[1])

    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])

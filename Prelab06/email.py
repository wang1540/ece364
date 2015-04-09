#! /usr/bin/env python3.4
import re

if __name__ == "__main__":

    with open('Part2.in','r') as f:
        lines = f.readlines()

    for line in lines:
        out = re.sub(r'(\w*)@(purdue.edu)([\t\s]*)(\d+\.\d+)', r'\1@ecn.\2\3\4/100',line)
        print(out)


# for ln in lines:
#     print(ln)
#     xx = re.search(r'(?P<user>\w*)@([\w\.]*)([\s\t]*)(\d+\.\d+)',ln)
#     if xx:
#         print(xx.group())
#         print('{}@ecn.purdue.edu/100'.format(line.group('user')))
#     # print()
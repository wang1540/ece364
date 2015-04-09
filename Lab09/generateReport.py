#! /usr/bin/env python3.4
__author__ = "Xihui Wang"

import re
from pprint import pprint as pp


def main():

    with open('rawGrades.xml','r') as f:
        lines = f.read()
    stuinfo = re.findall(r'<(.*)>(.*?):(.*)</(.*)>',lines)

    result = '<?xml version="1.0"?>\n<students>\n'

    for info in stuinfo:
        otag, name, coursestr, ctag = info

        if otag == ctag: 
            if ';' in coursestr:
                courselist = coursestr.split(';')
            else:
                courselist = coursestr.split(',')
            courses = {}
            for course in courselist:
                course = course.strip()[1:-1]
                cid, grade = course.split(':')
                courses[cid] = int(grade)
            final = []

            for k in courses.keys():
                letter = getLetter(courses[k])
                final = final + [(k, courses[k],letter)]
            final.sort()

            result += write(otag, name, final)
        else:
            pass
    result += '</students>'
    output(result)


def getLetter(grade):
    if grade in range(90,101):
        return 'A'
    elif grade in range(80,90):
        return 'B'
    elif grade in range(70,80):
        return 'C'
    elif grade in range(60,70):
        return 'D'
    else:
        return 'F'

def write(tag, name, grade):
    info = '   <student name="{}" id="{}">\n'.format(name, tag)
    gradestr = ''
    for ele in grade:
        k, score, letter = ele
        gradestr += '      <ECE{} score="{}" grade="{}"/>\n'.format(k, score, letter)
    overall = info + gradestr + '   </student>\n'
    return overall

def output(result):
    fout = open('finalGrades.xml','w')
    fout.write(result)
    fout.close()

if __name__ == "__main__":
    main()

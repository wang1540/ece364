#! /usr/bin/env python3.4
__author__ = "Xihui Wang"

values = input("Please enter some values: ")
value_list = values.split()
temp = []
for i in value_list:
    try:
        i = float(i)
        temp += [i]
    except ValueError:
        pass
print("The sum is: {}".format(sum(temp)))
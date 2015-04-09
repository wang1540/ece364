#! /usr/bin/env python3.4


def dotProduct(row, column):
    if type(row) is not list or type(column) is not list:
        raise TypeError("Row & Column must be lists.")
    if (len(row) == len(column)) and (len(row) > 0):
        raise ValueError("Row & Column must be of the same size.")
    print(row)
    print(column)


def test():
    a = input("Please enter some values: ")
    if a == 0:
        raise ValueError("oo")
    print("hehe")

if __name__ == '__main__':
    row2 = [3,7,1,8]
    column2 = [2,5,6,9]
    dotProduct(row2, column2)
    dotProduct(9, column2)
#! /usr/bin/env python3.4
__author__ = "Xihui Wang"


def find_median(input1, input2):
    merged = input1 + input2
    merged.sort()
    return merged[int((len(merged) - 1) / 2)], merged


def main():
    input1 = input ("Enter the first list of numbers: ")
    input2 = input ("Enter the second list of numbers: ")
    whole = input1.split() + input2.split()

    for ele in whole:
        try:
            ele = int(ele)
            list1 = [int(i) for i in input1.split()]
            list2 = [int(i) for i in input2.split()]
            print("First list: {}".format(list1))
            print("Second list: {}".format(list2))
            median, merged = find_median(list1, list2)
            print("Merged list: {}".format(merged))
            print("Median: {}".format(median))

        except ValueError:
            print("Input should be two sets of numbers, separated by whitespace")
            return

if __name__ == "__main__":
    main()

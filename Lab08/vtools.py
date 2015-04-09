#! /usr/bin/env python3.4
__author__ = "Xihui Wang"
import string
import re


def is_valid_name(identifier):

    # anyErrors = [c for c in identifier if c not in validSet]
    # return True if not anyErrors else False

    validSet = set(string.ascii_letters + string.digits + "_")
    diffSet = set(identifier) - validSet
    isEmpty = len(diffSet) == 0
    return isEmpty


def parse_pin_assignment(assignment):
    out = re.match(r'\.(.*)\((.*)\)', assignment)

    if not out:
        raise ValueError(assignment)

    port, pin = out.group(1), out.group(2)

    if not (is_valid_name(port) and is_valid_name(pin)):
        raise ValueError(assignment)

    return port, pin


def parse_net(line):

    out = re.search(r'(.*?)\((.*)\)', line)

    if not out:
        raise ValueError(line)

    name1, name2 = out.group(1).split()

    if not is_valid_name(name1) or not is_valid_name(name2):
        raise ValueError(line)

    elements = out.group(2).split(',')

    parsedLine = []

    for element in elements:

        element = element.strip()

        if not parse_pin_assignment(element):
            raise ValueError(line)

        parsedLine.append(parse_pin_assignment(element))

    return name1, name2, tuple(parsedLine)

if __name__ == "__main__":
    lien = 'DFFSR present_val_reg  ( .D(n30), .CLK(clk), .R(n33), .S(1), .Q(stop_bit) )'

#! /usr/bin/env python3.4
import math

class Point2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def dist_between(self, other):
        # Compute the distance between this point and another point
        xsq = (self.x - other.x) * (self.x - other.x)
        ysq = (self.y - other.y) * (self.y - other.y)
        return math.sqrt(xsq + ysq)

    def pointlist (self):
        plist = [Point2D(x+1, y+1) for x in range(10) for y in range(10)]
        return plist

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class MyPoint2D(Point2D):
    def __init__(self, x=0.0, y=0.0):
        Point2D.__init__(self, x, y)

    def get_max_coord(self):
        return max(self.x, self.y)

    def get_min_coord(self):
        return min(self.x, self.y)
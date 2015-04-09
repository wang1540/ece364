
#! /usr/bin/env python3.4

__author__ = 'ee364e13'

import math


class Point3D:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return "({:.2f}, {:.2f}, {:.2f})".format(round(self.x,2), round(self.y, 2), round(self.z, 2))

    def disFrom(self, other):
        xsq = (self.x - other.x) * (self.x - other.x)
        ysq = (self.y - other.y) * (self.y - other.y)
        zsq = (self.z - other.z) * (self.z - other.z)

        return math.sqrt(xsq + ysq + zsq)


    def nearestPoint(self, points):
        if len(points) == 0:
            return None

        distance = -1
        for point in points:
            if distance == -1:
                distance = self.disFrom(point)
                ret = point
            else:
                if self.disFrom(point) < distance:
                    distance = self.disFrom(point)
                    ret = point

        return ret

    def clone(self):
        return Point3D(self.x, self.y, self.z)


    def __add__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

        if isinstance(other, float):
            return Point3D(self.x + other, self.y + other, self.z + other)

        return None

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, float):
            return Point3D(self.x - other, self.y - other, self.z - other)

        return None

    def __neg__(self):
        return Point3D(-self.x, -self.y, -self.z)

    def __truediv__(self, other):
        if isinstance(other, float):
            return Point3D(self.x / other, self.y / other, self.z / other)

        return None

    def __mul__(self, other):
        if isinstance(other, float):
            return Point3D(self.x * other, self.y * other, self.z * other)

        return None

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            return None
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __gt__(self, other):
        if not isinstance(other, Point3D):
            return None
        return self.disFrom(Point3D()) > other.disFrom(Point3D())

    def __ge__(self, other):
        if not isinstance(other, Point3D):
            return None
        return self.disFrom(Point3D()) >= other.disFrom(Point3D())

    def __lt__(self, other):
        if not isinstance(other, Point3D):
            return None
        return self.disFrom(Point3D()) < other.disFrom(Point3D())

    def __le__(self, other):
        if not isinstance(other, Point3D):
            return None
        return self.disFrom(Point3D()) <= other.disFrom(Point3D())

    def __hash__(self):
        pointTuple = self.x, self.y, self.z
        return hash(pointTuple)



class PointSet:

    def __init__(self, points=set()):
        self.points = set(points)

    def __str__(self):
        if not self.points:
            return "Empty"
        str = ""
        for point in self.points:
            str = str + "   " + point.__str__()
        return str.strip()


    def addPoint(self, p):
        if isinstance(p, Point3D):
            self.points.add(p)

    def count(self):
        return len(self.points)

    def computeBoundingBox(self):
        if len(self.points) == 0:
            return None

        x_max = 0
        y_max = 0
        z_max = 0
        x_min = float("inf")
        y_min = float("inf")
        z_min = float("inf")

        for point in self.points:
            if point.x > x_max:
                x_max = point.x
            elif point.x < x_min:
                x_min = point.x

            if point.y > y_max:
                y_max = point.y
            elif point.y < y_min:
                y_min = point.y

            if point.z > z_max:
                z_max = point.z
            elif point.z < z_min:
                z_min = point.z

        point_max = Point3D(x_max, y_max, z_max)
        point_min = Point3D(x_min, y_min, z_min)

        retTuple = point_max, point_min

        return retTuple

    def computeNearestNeighbors(self, other):
        if not isinstance(other, PointSet):
            return None

        retList = []

        for mypoint in self.points:
            distance = float("inf")

            for otherpoint in other.points:

                if mypoint.disFrom(otherpoint) < distance:

                    distance = mypoint.disFrom(otherpoint)
                    Neighbor = otherpoint

            retTuple = mypoint, Neighbor
            retList.append(retTuple)

        return retList



    def __add__(self, other):
        if isinstance(other, Point3D):
            retSet = PointSet(self.points)
            return retSet.addPoint(Point3D)

        if isinstance(other, PointSet):
            retSet = PointSet(self.points)
            for point in other.points:
                retSet.addPoint(point)

            return retSet

        return None

    def __sub__(self, other):
        if isinstance(other, Point3D):
            retSet = PointSet(self.points)
            retSet.points.discard(other)
            return retSet

        if isinstance(other, PointSet):
            retSet = PointSet(self.points)
            for point in other.points:
                retSet.points.discard(point)
            return retSet

        return None

    def __gt__(self, other):
        if not isinstance(other, PointSet):
            return None

        return self.count() > other.count()

    def __ge__(self, other):
        if not isinstance(other, PointSet):
            return None

        return self.count() >= other.count()

    def __lt__(self, other):
        if not isinstance(other, PointSet):
            return None

        return self.count() < other.count()


    def __le__(self, other):
        if not isinstance(other, PointSet):
            return None

        return self.count() <= other.count()




if __name__ == "__main__":

    point1 = Point3D(1,1,1)
    point2 = Point3D(2.12,3.28,1.75)


    print(point1)


    print(point1.disFrom(point2))


    A = point1 + point2
    B = point1 + 2.1231
    #C = 1.123 + point1
    B1 = 2.1231 + point1


    C = point2 - point1
    D = point1 - 1.0

    E = -point1
    F = point2 / 2.0

    G = point1 * 4.8
    H = 4.8 * point1


    print(A)
    print(B)
    print(B1)
    print(C)
    print(D)
    print(E)
    print(F)
    print(G)
    print(H)

    print(point2 > point1)
    print(point2 >= point1)
    print(point2 < point1)
    print(point2 <= point1)

    mylist = [A, B, C]
    myset = set(mylist)
    myOtherList = [D, E, F]
    myOtherSet = set(myOtherList)
    #print(myset)

    myPset2 = PointSet(mylist)


    myPointset = PointSet(myset)
    myOtherPointset = PointSet(myOtherSet)

    myPointset.computeBoundingBox()
    #print(myPointset)
    retList = myPointset.computeNearestNeighbors(myOtherPointset)
    for Tup in retList:
        print("{0}, {1}".format(Tup[0], Tup[1]))

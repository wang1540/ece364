#! /usr/bin/env python3.4

import operator


class Point3D:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return "({:.2f}, {:.2f}, {:.2f})".format(round(self.x, 2), round(self.y, 2), round(self.z, 2))

    def disFrom(self, other):
        if not isinstance(other, Point3D):
            return None
        return pow((pow((self.x-other.x), 2) + pow((self.y-other.y), 2) + pow((self.z-other.z), 2)), 0.5)

    def nearestPoint(self, points):
        if (not isinstance(points, list) and not isinstance(points, set)) or len(points) == 0:
            return None

        # distances = [(index, self.disFrom(point)) for index, point in enumerate(points)]
        # distances.sort(key=operator.itemgetter(1))
        # targetIndex, _ = distances[0]
        #
        # return points[targetIndex]

        minDist = float("inf")
        for point in points:
            if not isinstance(point, Point3D):
                return None
            if self.disFrom(point) < minDist:
                nestP = point
                minDist = self.disFrom(nestP)
        return nestP

    def clone(self):
        copypt = Point3D(self.x, self.y, self.z)
        return copypt

    def __add__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, float):
            return Point3D(self.x + other, self.y + other, self.z + other)
        else:
            return None

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, float):
            return Point3D(self.x - other, self.y - other, self.z - other)
        else:
            return None

    def __neg__(self):
        return Point3D(-self.x, -self.y, -self.z)

    def __truediv__(self, other):
        if not isinstance(other, float):
            return None
        return Point3D(self.x / other, self.y / other, self.z / other)

    def __mul__(self, other):
        if not isinstance(other, float):
            return None
        return Point3D(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            return None
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __gt__(self, other):
        if not isinstance(other, Point3D):
            return None
        return True if (self.disFrom(Point3D()) > other.disFrom(Point3D())) else False

    def __ge__(self, other):
        if not isinstance(other, Point3D):
            return None
        return True if (self.disFrom(Point3D()) >= other.disFrom(Point3D())) else False

    def __lt__(self, other):
        if not isinstance(other, Point3D):
            return None
        return False if self.__ge__(other) else True

    def __le__(self, other):
        if not isinstance(other, Point3D):
            return None
        return False if self.__gt__(other) else True

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
        return self.points.add(p) if isinstance(p, Point3D) else None

    def count(self):
        return len(self.points)

    def computeBoundingBox(self):
        if len(self.points) == 0:
            return None
        xbox = [i.x for i in self.points]
        ybox = [i.y for i in self.points]
        zbox = [i.z for i in self.points]

        xbox.sort()
        ybox.sort()
        zbox.sort()

        size = len(xbox) - 1

        return Point3D(xbox[size], ybox[size], zbox[size]), Point3D(xbox[0], ybox[0], zbox[0])

    def computeNearestNeighbors(self, other):
        if not isinstance(other, PointSet) or len(other.points) == 0:
            return None
        if not self.points:
            return None
        l = []
        for point in self.points:
            if point.nearestPoint(other.points) == None:
                return None
            l += [(point, point.nearestPoint(other.points))]
        return l

    def __add__(self, other):
        if isinstance(other, PointSet):
            temp = PointSet(self.points)
            for point in other.points:
                temp.points.add(point)
            return temp
        elif isinstance(other, Point3D):
            temp = PointSet(self.points)
            temp.points.add(other)
            return temp
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, PointSet):
            return PointSet(self.points.difference(other.points))
        elif isinstance(other, Point3D):
            return PointSet(self.points.difference([other]))
        else:
            return None

    def __gt__(self, other):
        if not isinstance(other, PointSet):
            return None
        return True if self.count() > other.count() else False

    def __ge__(self, other):
        if not isinstance(other, PointSet):
            return None
        return True if self.count() >= other.count() else False

    def __lt__(self, other):
        if not isinstance(other, PointSet):
            return None
        return False if self.__ge__(other) else True

    def __le__(self, other):
        if not isinstance(other, PointSet):
            return None
        return False if self.__gt__(other) else True

    def __eq__(self, other):
        if not isinstance(other, PointSet):
            return None
        return True if self.count() == other.count() else False

#! /usr/bin/env python3.4
from MorePoints import *

def test1():
    point1 = Point3D()
    point2 = Point3D(1,1,4)
    point3 = Point3D(1,1,1)
    point4 = Point3D(2,1,0)
    point5 = Point3D(0,3,0)
    s=[point2,point3,point4,point5]


    print("Test point3d")
    print(point1.disFrom(point2))
    print(point1.disFrom(point3))
    print(point1.disFrom(point4))

    print("nearest\n")
    print(point1.nearestPoint(s))
    print(point1.nearestPoint([]))
    print(point1)
    print(point1.nearestPoint([point1, point3]))
    print("\n")

    print(point1+point2+6.0+point3)
    print(point1+point2+point3+6)
    print(-point3)
    print("aaa")
    print(point2 - point3 - 1.0)
    print("bbb")
    print(point2 * 3.0 / 3.0)
    print(3 *point2)

    print(point2 == point2.clone)
    print(point2 == point3)
    print(point2 > point3)
    print(point2 <= point3)
    print(point2 >= point3)

def test2():
    print("test for pointset")
    set1=PointSet()
    print(set1)
    ss=s+[point3]
    set2 = PointSet(s)
    print(set2.count())
    set3 = PointSet(ss)
    print("3 is {}".format(set3.count()))
    print(set1.count())
    p1,p2=set2.computeBoundingBox()
    print(p1)
    print(p2)
    print(set1.computeBoundingBox())
    set4 = PointSet([point5, point2])
    p1,p2 = set4.computeBoundingBox()
    print(p1)
    print("aaa")
    print(p2)
    print("bbgb")

    sset = PointSet([point1, point2, point3, point4, point5, point1])
    print(sset)
    print(sset.count())
    print(sset.computeBoundingBox())
    print(type(sset.computeBoundingBox()))
    p,q = sset.computeBoundingBox()
    print("{} and {}".format(p,q))
    print("aa")
    print(sset.computeNearestNeighbors(tuple([point1, point2, point3, point4, point5, point1])))
    print("bb")
    sett = PointSet([point1, point2, point3, point4, point5, point1])
    print(type(sett.points))
    for T in sset.computeNearestNeighbors(sett):
        p,q = T
        print("{} and {}".format(p,q))

    print(sset > set3)
    print(sset == set3)
    print(sset >= set3)
    print(sset < set3)
    print(sset <= set3)
    print(sset < 4)
    print(sset + set3)




if __name__ == "__main__":
    point1 = Point3D()
    point2 = Point3D(1,1,4)
    point3 = Point3D(1,1,1)
    point4 = Point3D(2,1,0)
    point5 = Point3D(0,3,0)
    s=[point2,point3,point4,point5]
    test1()

"""
from MorePoints import *
point1 = Point3D()
point2 = Point3D(1,1,4)
point3 = Point3D(1,1,1)
point4 = Point3D(2,1,0)
point5 = Point3D(0,3,0)
s=[point2,point3,point4,point5]
sset = PointSet([point1, point2, point3, point4, point5, point1])
set1=PointSet()
set2=PointSet([point1])
print(set1 - point1)
print(set1 - sset)

"""

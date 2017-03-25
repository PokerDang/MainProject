# encoding: utf-8

import math

class Point(object):
    def __init__(self,xParam=0.0,yParam=0.0):
        self.x=xParam
        self.y=yParam

    def distance(self,pt):
        xDiff = self.x - pt.x
        yDiff = self.y - pt.y

        return math.sqrt(xDiff**2+yDiff**2)

    def sum(self,pt):
        newPt = Point()
        newPt.x = self.x + pt.x
        newPt.y = self.y + pt.y
    def __str__(self):
        return "(%.2f, %.2f)"% (self.x,self.y)
    


def main():
    p1 = Point(2.0,4.0)
    p2 = Point()
    print p1.distance(p2)
    print p1
main()
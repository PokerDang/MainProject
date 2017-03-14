# encoding: utf-8

import math

class Point(object):
    def __init__(self):
        self.x=0.0
        self.y=0.0

    def distance(self,pt):
        xDiff = self.x - pt.x
        yDiff = self.y - pt.y

        return math.sqrt(xDiff**2+yDiff**2)

    def sum(self,pt):
        newPt = Point()
        newPt.x = self.x + pt.x
        newPt.y = self.y + pt.y

def main():
    p1 = Point()
    p2 = Point()
    print p1.x, p1.y

main()
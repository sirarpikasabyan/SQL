#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nirvana
#
# Created:     13/06/2014
# Copyright:   (c) Nirvana 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from math import sqrt

class Point(object):
    x=0
    y=0

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def self_location(self, x, y):
        self.x=x
        self.y=y

    def distance_from_origin(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def distance(self, other):
        dx=self.x-other.x
        dy=self.y-other.y
        return sqrt(dx*dx+dy*dy)

    def translate(self, dx, dy):
        self.x+=dx
        self.y+=dy

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

mypoint = Point(4,5)
t1 = mypoint.distance_from_origin()
print(t1)
yourpoint = Point(1,3)
t2 = yourpoint.distance_from_origin()
print(t2)
t3 = mypoint.distance(yourpoint)
print(t3)

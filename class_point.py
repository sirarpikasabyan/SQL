#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nirvana
#
# Created:     14/06/2014
# Copyright:   (c) Nirvana 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Point:
    'class that represents a point in the plane'
    x1 = 0
    y1 = 0

    def __init__(self,xcoord=0,ycoord=0):
        self.x=xcoord
        self.y=ycoord

    def get(self):
        "return coordinates of the point"
        return (self.x,self.y)

    def move(self, dx, dy):
        self.x+=dx
        self.y+=dy

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def __eq__(self, other):
        return self.x == other.x and self.y==other.y

    def __repr__(self):
        return "point({}, {})".format(self.x, self.y)

    def __str__(self):
        return "point({}, {})".format(self.x, self.y)

    def __add__(self, otherpoint):
        return Point(self.x + otherpoint.x,self.y + otherpoint.y)


point1=Point(1,1)
point2=Point(1,1)
point3 = point1 + point2
print(point3)
print (point1==point2)


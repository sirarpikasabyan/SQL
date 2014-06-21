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
import class_point

class Point3D(class_point.Point):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z=z

    def move(self, dx, dy, dz):
        super().move(dx, dy)
        self.z += dz

mypoint=Point3D(3,4,5)
mypoint.move(1,1,1)
print (mypoint)


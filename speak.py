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

class Animal(object):

    def __init__(self, species = "animal", language = "make sounds"):
        self.species=species
        self.language=language

    def speak(self):
        return ("I am a {} and I {} ".format(self.species,self.language))

snoopy = Animal("dog")
print (snoopy.speak())

class Bird(Animal):

    def speak(self):
        return ("{}!".format(self.language * 3))

mybird = Bird("bird","tweet")
print (mybird.speak())
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nirvana
#
# Created:     07/06/2014
# Copyright:   (c) Nirvana 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

class Coin(object):
    def __init__(self):
        self.sideup = "Heads"

    def toss(self):
        if random.randint(0,1)==0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup

mycoin=Coin()
print (mycoin.sideup)
print (mycoin.get_sideup())
mycoin.toss()
print (mycoin.get_sideup())

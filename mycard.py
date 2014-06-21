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

class Card(object):

    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __repr__(self):
        return "point({}, {})".format(self.rank, self.suit)


mycard1=Card("Joker", "\u2660")
mycard2=Card("Joker", "\u2660")
print (mycard1==mycard2)


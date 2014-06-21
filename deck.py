from mycard import *
import random

class Deck(object):

    ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
    suits = {"\u2660","\u2661", "\u2662", "\u2663"}

    def __init__(self):
        self.cards=[]
        for rank in self.ranks:
            for suit in self.suits:
                card = Card(rank, suit)
                self.cards.append(card)


    def shuffle(self):
        random.shuffle(self.cards)


    def dealCard(self):
        return self.cards[0]


deck=Deck()
print (deck.cards[0])
deck.shuffle()
print (deck.cards[0])
newcard=deck.dealCard()
print (newcard)





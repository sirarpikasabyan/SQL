#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nirvana
#
# Created:     21/06/2014
# Copyright:   (c) Nirvana 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Queue(object):

    def __init__(self):
        self.list = []

    def __len__(self):
        return self.list.__len__()

    def enqueue(self, name):
        self.list.append(name)

    def dequque(self):
        return self.list.pop(0)

    def isEmpty(self):
        if len(self.list)==0:
            return True
        else:
            return False

appts = Queue()
appts.enqueue("John")
appts.enqueue("valod")
appts.enqueue("vaxarshak")
print (appts.dequque())
print (appts.isEmpty())

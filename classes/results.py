import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from classes.item import item

class results(object):
 def __init__(self, resultList, infos, parserType, error,  url): 
    self.resultList = resultList
    self.info = infos
    self.type = parserType
    self.error = error
    self.url = url

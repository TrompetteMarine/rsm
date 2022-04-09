import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# importing
from type3 import parseType3
  
f = open(currentdir + "/fixture.txt", "r")
parseType3(f.read())
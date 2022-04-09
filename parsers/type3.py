import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import re
import string

from bs4 import BeautifulSoup
from classes.item import item
from classes.results import results


#parser type = texte
def parseType3(htmlDocument): 
 
    
    finalResults = results([],"",-1)
    #strip html tag
    p = re.compile(r'<.*?>')
    strippedDoc =  p.sub('', htmlDocument)

    strippedDoc =  strippedDoc.replace('\\n',"")

    strippedDoc =  strippedDoc.replace('&nbsp',"")

    strippedDoc =  strippedDoc.replace('&amp',"")

    allow = string.ascii_letters  + " " + '-' # + string.digits 

    finalStrippedDoc = re.sub('[^%s]' % allow, '', strippedDoc)

    #finalStrippedDoc =  strippedDoc.replace('\\n',"")

    print(finalStrippedDoc)

    finalResults = results([],"",-1)

    finalResults.resultList.append(item("doc",finalStrippedDoc))
    
    finalResults.info ="type3"
    finalResults.parserType = 3

    return  finalResults 

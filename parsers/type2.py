from bs4 import BeautifulSoup
from classes.item import item
from classes.results import results

def parseType2(table):

 try:
  finalResults = results([],"",-1)
  for t in table:
        #looking for Item... = title
        if (t.text.find('Item') != -1): 
        #looking for all next <p> that contain the body of the item (loop until the next <table)
            p=""
            #emulate do loop ... :(
            tag = t
            
            while True:
                np = tag.findNext('div')
                if(np.text != '\xa0'):
                    p += "\n" + np.text
                    tag=tag.findNext('div')
                else:
                    break
                #create final object and store it in an array
            finalResults.resultList.append(item(t.text,p))

  finalResults.info = "type2"
  finalResults.parserType = 2

 except:
  finalResults.info = "error"

 return finalResults
from bs4 import BeautifulSoup
from classes.item import item
from classes.results import results

def parseType1(table):

 finalResults = results([],"",-1)

 for t in table:
    #looking for Item... = title
    if (t.text.find('Item') != -1): 
    #looking for all next <p> that contain the body of the item (loop until the next <table)
        p= ""
        #emulate do loop ... :(
        tag = t
                    
        while True:
            np = tag.findNext('p')
            if np == None :
                np = tag.findNext('div')
            if np == None :
                print("Parsing Error")
                break
            if(np.text != '\xa0'):
                p += "\n" + np.text
                tag=tag.findNext('p')
            if np == None :
                np = tag.findNext('div')
            else:
                break
        #create final object and store it in an array
        finalResults.resultList.append(item(t.text,p))

 finalResults.info ="type1"
 finalResults.parserType = 1

 return finalResults
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests as req
from urllib.parse import urlparse
from os.path import splitext
from classes.item import item
from parsers.type1 import parseType1
from parsers.type2 import parseType2
from classes.results import results

def browse(url):
 finalResults = results([],"")
 
 #get the domain part of the url
 domain = urlparse(url).netloc
 #init webdriver
 browser = webdriver.Chrome()
 #browse to the url
 browser.get(url)
 #get hml content
 html = browser.page_source

 #extract HTML Link 
 soup = BeautifulSoup(html, features="html.parser")
 #research for all the <p> tag
 for p in soup.find_all('a'):
   
   #TODO: change the way we retrieve the 8k filename.
   if (p.text.find('8vk.htm')!= -1 or p.text.find('8k.htm')  != -1 or p.text.find('8k')  != -1):

        ext = splitext(p.text)[1]
        if ext == ".txt":
            print("page is a text file, cannot extract any data")
            break

        #extract local url from html tag.
        documentUrl = p.get("href")
        #construct url & open the child document
        browser.get("https://" + domain + documentUrl )
        #get html from child document
        documentHtml = browser.page_source
        #extract for BeautifulSoup
        docSoup = BeautifulSoup(documentHtml, features="html.parser")
         
        #1) find table (title)
        table = docSoup.find_all('table')
        parserType = 1

        isOldDocument = docSoup.find('p')
        if isOldDocument == None:
            parserType =2

        if parserType == 1:  #parse type = <p>
            finalResults = parseType1(table)
        elif parserType == 2:
            finalResults = parseType2(table)

        #we found 1 file, not necesary to continue the for loop
        break

 #check if its ok...
 if finalResults != None:
    for obj in finalResults.resultList:
        print( obj.title, obj.body, sep =' ' )

 browser.close()

 return(finalResults)
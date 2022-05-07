from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests as req
from urllib.parse import urlparse
from os.path import splitext
from classes.item import item
from parsers.type3 import parseType3
from classes.results import results

#Option for headless chrome

debugMode = False

if debugMode == True :
    options = Options()
    options.add_argument("no-sandbox")
    options.add_argument("headless")
    options.add_argument("start-maximized")
    options.add_argument("window-size=1900,1080")
else :
    options = None

def browseTxtMode(url):
 finalResults = results([],"", -1,"","")
 
 #get the domain part of the url
 domain = urlparse(url).netloc
 #init webdriver
 browser = webdriver.Chrome(chrome_options=options)
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


        #extract local url from html tag.
        documentUrl = p.get("href")
        #construct url & open the child document
    
        _8KUrl = "https://" + domain + documentUrl

        browser.get(_8KUrl)
        #get html from child document
        documentHtml = browser.page_source

        finalResults = parseType3(documentHtml)


        finalResults.url = _8KUrl
        #we found 1 file, not necesary to continue the for loop
        break
  

 #check if its ok...
 """if finalResults != None:
    for obj in finalResults.resultList:
        print( obj.title, obj.body, sep =' ' )"""

 browser.close()

 return(finalResults)
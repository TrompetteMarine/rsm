from csvImport import importCSV
from browse import browse
from browseTxtMode import browseTxtMode
import os
from classes.results import results
from classes.stats import stats
import random as rnd
from analyze import analyze 
from analyze import tokenize
from classes.score import score as Score
import csv

big_data=[]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def process(count, start, end, offset):
    if end<start:
        print("Error end < start")

    # import csv data
    listToImport = importCSV("to_use_text.csv",  start, end, offset)

    nothing = 0

    cls()

    numType1 = 0
    numType2 = 0
    numType3 = 0
    parserError = 0

    for url in listToImport:
        
        #extract data from url 
        print("\n##############################################################")    
        print("Extract Report for: " + url[0])
        print("\n")

        results = browseTxtMode(url[0])
        
        if hasattr(results, 'parserType'):
            if results.parserType == 1:
                numType1 +=1
            if results.parserType == 2:
                numType2 +=1  
            if results.parserType == 3:
                numType3 +=1
        else:
            parserError +=1 

        
        if( (len(results.resultList)>0) and (len(results.error)==0)) :
            item =  results.resultList[0]
        elif(len(results.error)>0):
            print(results.error)


       
        tokenText= tokenize(item.body)
        Score = analyze(tokenText)

        #log
        print("\n--------------------------------------------------------------")    
        print("Extracted with parser of type: " + results.info) 
        count+=1
        print("Extract num: "+ str(count) + "/" + str(end-start))
        print("\n")
        if len(results.resultList) == 0:
            print("Nothing Extracted, please check format or/and content of the page")
            nothing+=1
            print("\n---------------------------------------------------------")
            
        print("TOTAL PAGE(s) EXTRACTED :" + str(count - nothing))
        print("TOTAL PAGE(s) WITHOUT RESULT " + str(nothing))

        successRatio = 100-(nothing*(100/count))

        print("\nSUCCES RATIO:" + str(int(successRatio)) +"%")
        print("\n---------------------------------------------------------")

        print ("parser 1 ratio : " + str(numType1*(100/count)))
        print ("\nparser 2 ratio : " + str(numType2*(100/count)))
        print ("\nResult for file : " +  url[0])

        print ("\nPositive word(s) : " +  str(Score.positive))
        print ("\nNegative words(s) : " +  str(Score.negative))
        

        stats(0,0,0,0)
        stats.type1 = numType1*(100/count)
        stats.type2 = numType2*(100/count)
        stats.type3 = numType3*(100/count)
        #stats.positive = 
        stats.error = results.error

        f = open('stat.txt', 'a') 
        f.write('\n---------------------------------------------------------')
        f.write("\nFile : " +  url[0])
        f.write("\n8K File : " +  results.url)
        f.write("\nPositive word(s) : " + str(Score.positive))
        f.write("\nNegative word(s) : " + str(Score.negative))
        f.close()
    
        #save value in csv file
        #header = ['file', '8Kfile', 'score +', 'score -', 'word +', 'word -']
        data = [url[0], results.url, str(Score.positive), str(Score.negative),"",""]

        with open('statResult.csv', 'a', newline='') as csvfile:
            statWriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            statWriter.writerow(data)

    return stats
  
  
# importCSV
# 
# params:
#  dataSource, csv file
#  start: first entry to browse 
#  end: last entry to browse
#  offset: first page browsed is retrieved at entry number (offset + start)
count = 0
for x in range(1) :

    offset = 100 # int(rnd.random() * 600000)
    start = 0
    end = 5
    stats = process(count, start, end, offset)
    count = 0

    #save stats        
    f = open('stat.txt', 'a') 
    f.write('\n---------------------------------------------------------')
    f.write('\n From #' + str(start+offset) + 'to: ' +str(end + offset))
    f.write("\nparser 1 ratio : " + str(stats.type1))
    f.write("\nparser 2 ratio : " + str(stats.type2))
    f.write("\nparser 3 ratio : " + str(stats.type3))
    f.write("\nparser error : " + str(stats.error))
    f.close()
from csvImport import importCSV
from browse import browse
import os
from classes.results import results

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# importCSV
# params:
#  dataSource, csv file
#  start: first entry to browse 
#  end: last entry to browse
#  offset: first page browsed is retrieved at entry number (offset + start)
big_data=[]
offset = 0
start = 5
end = 14

if end<start:
    print("Error end < start")

# import csv data
listToImport = importCSV("to_use_text.csv",  start, end, offset)
count = 0
nothing = 0

cls()

for url in listToImport:
    
    #extract data from url 
    print("\n##############################################################")    
    print("Extract Report for: " + url[0])
    print("\n")

    results = browse(url[0])

    #append data
    big_data.append(results)

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
    #save big_data to file
    #print(big_data)
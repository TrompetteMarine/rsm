from csvImport import importCSV
from browse import RSM
import os
#import csv as csvReader

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# importCSV
# params:
#  dataSource, csv file
#  start: first entry to browse 
#  end: last entry to browse
#  offset: first page browsed is retrieved at entry number (offset + start)
big_data=[]
offset = 99900
start = 0
end = 5

# import csv data
listToImport = importCSV("to_use_text.csv",  start, end, offset)

count = 0
nothing = 0

cls()

for url in listToImport:
    
    #extract data from url 
    result = RSM(url[0])

    #append data
    big_data.append(result)

    #log
    print("Extract of: " + url[0]) 
    print("\n")
    count+=1
    print("Extract num: "+ str(count) + "/" + str(end-start))
    if len(result) == 0:
        print("\n")
        print("Nothing Extracted, please check format or/and content of the page")
        nothing+=1
        print("\n---------------------------------------------------------")
        
    print("TOTAL PAGE(s) EXTRACTED :" + str(count - nothing))
    print("\n TOTAL PAGE(s) WITHOUT RESULT " + str(nothing))

    successRatio = 100-(nothing*(100/count))

    print("\n Success :" + str(int(successRatio)) +"%")
    print("\n---------------------------------------------------------")

    #save big_data to file
    #print(big_data)
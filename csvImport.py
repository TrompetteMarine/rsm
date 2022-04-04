#here: importation of csv contents.
import pandas as pd
import os
#import csv as csvReader
from browse import RSM

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def importCSV(csvFile, start, end, offset):
    offset =offset
    startLine = offset + start
    endLine = offset + end
    big_data=[]

    #pandas.read_csv()
    reviews_df = pd.read_csv("to_use_text.csv", skiprows=startLine, nrows=endLine-startLine, usecols=[0])

    #for performances purpose
    urlList =  reviews_df.values.tolist() 

    count = startLine - offset
    nothing = 0

    cls()

    for url in urlList:
        result = RSM(url[0])
        big_data.append(result)

        print("Extract of: " + url[0])
        print("\n")
        count+=1
        print("Extract num: "+ str(count) + "/" + str(endLine-startLine))
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
    

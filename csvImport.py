#here: importation of csv contents.
import pandas as pd
def importCSV(csvFile, start, end, offset):
    offset =offset
    startLine = offset + start
    endLine = offset + end
 
    #pandas.read_csv()
    reviews_df = pd.read_csv("to_use_text.csv", skiprows=startLine, nrows=endLine-startLine, usecols=[0])

    #for performances purpose
    urlList =  reviews_df.values.tolist() 
    return urlList
    

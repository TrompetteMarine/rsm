#import xml.etree.ElementTree as ET
#import math
#import time
#import numpy as np
import pandas as pd
#import re
#import os
import nltk
#from datetime import date

from nltk.corpus import sentiwordnet as swn
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import WordPunctTokenizer as wpt

#import pysentiment as ps

#hiv4 = ps.HIV4()
#from textblob import TextBlob

#Load Loughran McDonald Sentiment classifier file
sentiment_dataframe = pd.read_csv("LoughranMcDonald_MasterDictionary_2018.csv")

dataset = pd.read_csv("test2.csv",usecols=[0]) #pd.read_csv("test.csv", skiprows=0, usecols=[0]) #pd.read_csv("test.csv")
sentence = dataset.iloc[:,0]
#print (dataset.iloc[:4])
nltk.download('punkt')
nltk.download('stopwords')
#nltk.download('corpus')
#token = nltk.word_tokenize(sentence)
#tagged = nltk.pos_tag(token)
#useless_words = ["the", "to", "'s" , "of", "by", "that", "this"]

"""Output = pd.DataFrame()
sentiment_list_quote = []
subjectivity_list_quote =[]
positive_words_list_quote = []
negative_words_list_quote = []
Quote_list = []
sentiment_list_FT = []
subjectivity_list_FT = []
positive_words_list_FT = []
negative_words_list_FT = []
Full_Text_list = []
StoreID_list = []
pysent_text_scores = []
pysent_quote_scores = []
Academic_ID_list = [] """

#convert to list for performances purpose
wordList =  sentence.values.tolist()

#Filter out only positive and negative words
positive_DF = sentiment_dataframe[sentiment_dataframe["Positive"]>0]
negative_DF = sentiment_dataframe[sentiment_dataframe["Negative"]>0]

#Convert the dataframes to lists and make them lowercase
positive_words = positive_DF["Word"].to_list()
positive_words = [word.lower() for word in positive_words]

negative_words = negative_DF["Word"].to_list()
negative_words = [word.lower() for word in negative_words]

for word in wordList:
	if word.lower() in positive_words:
		 print("Positive word Found in list: ", word)
	elif word.lower() in negative_words:
		 print("Negative word Found in list: ", word)

"""#Sentiment Analysis
for o in dataset.index -1:
	print(o)
	working_dataframe = Dataset.loc[Dataset["StoreID"] == Dataset.iloc[o]["StoreID"]]

	print(working_dataframe)

	working_DF_length = len(working_dataframe.index)

	#----------------------------Analyze Text----------------------------
	full_text_without_quote = ""

	if working_DF_length > 1:
		
		#Remove Quote
		t = 0
		full_text_without_quote = working_dataframe.iloc[0]["Full_Text"]
		while t < working_DF_length:
			full_text_without_quote = full_text_without_quote.replace(Dataset.iloc[t]["Quote"], " ")
			t = t+1

		#pysentiment module
		tokens_text = hiv4.tokenize(full_text_without_quote)
		pysent_score_text = hiv4.get_score(tokens_text)

		#Subjectivity text
		texblob_text = TextBlob(full_text_without_quote)
		subjectivity_score_text = texblob_text.sentiment.subjectivity

		#tokenize Text with lowercase letters
		tokenized_text = wpt().tokenize(full_text_without_quote)
		tokenized_text = [word.lower() for word in tokenized_text]


		#Create List of all negative and positive words found in the quote
		positive_words_text = [word for word in tokenized_text if word in positive_words]
		negative_words_text = [word for word in tokenized_text if word in negative_words]

		#Calculate sentiment score for the text
		if len(positive_words_text) == 0 and len(negative_words_text) == 0:
			sentiment_score_text = 0
		else:
			sentiment_score_text = (len(positive_words_text) + (-len(negative_words_text)))/(len(positive_words_text) + len(negative_words_text))

		#Add Values to list for Output
		if Dataset.iloc[o]["StoreID"] in StoreID_list:
			print("Already saved")
		else:
			Full_Text_list.insert(0, Dataset.iloc[o]["Full_Text"])
			sentiment_list_FT.insert(0, sentiment_score_text)
			positive_words_list_FT.insert(0, len(positive_words_text))
			negative_words_list_FT.insert(0, len(negative_words_text))
			pysent_text_scores.insert(0, pysent_score_text)
			subjectivity_list_FT.insert(0, subjectivity_score_text)

	else:

		#pysentiment module
		tokens_text = hiv4.tokenize(Dataset.iloc[o]["Full_Text"])
		pysent_score_text = hiv4.get_score(tokens_text)

		#Subjectivity text
		texblob_text = TextBlob(Dataset.iloc[o]["Full_Text"])
		subjectivity_score_text = texblob_text.sentiment.subjectivity

		#tokenize Text with lowercase letters
		tokenized_text = wpt().tokenize(Dataset.iloc[o]["Full_Text"])
		tokenized_text = [word.lower() for word in tokenized_text]

		#Create List of all negative and positive words found in the quote
		positive_words_text = [word for word in tokenized_text if word in positive_words]
		negative_words_text = [word for word in tokenized_text if word in negative_words]

		#Calculate sentiment score for the text
		if len(positive_words_text) == 0 and len(negative_words_text) == 0:
			sentiment_score_text = 0
		else:
			sentiment_score_text = (len(positive_words_text) + (-len(negative_words_text)))/(len(positive_words_text) + len(negative_words_text))

		#Add Values to list for Output
		if Dataset.iloc[o]["StoreID"] in StoreID_list:
			print("Already saved")
		else:
			Full_Text_list.insert(0, Dataset.iloc[o]["Full_Text"])
			sentiment_list_FT.insert(0, sentiment_score_text)
			positive_words_list_FT.insert(0, len(positive_words_text))
			negative_words_list_FT.insert(0, len(negative_words_text))
			pysent_text_scores.insert(0, pysent_score_text)
			subjectivity_list_FT.insert(0, subjectivity_score_text)
		

	#----------------------------Analyze Quotes----------------------------
	if working_DF_length > 1:

		#Add all quotes together
		q = 0
		all_quotes = ""
		while q < working_DF_length:
			all_quotes = all_quotes + " " + working_dataframe.iloc[q]["Quote"]
			q = q+1

		#pysentiment module
		tokens_quote = hiv4.tokenize(all_quotes)
		pysent_score_quote = hiv4.get_score(tokens_text)
		
		#Subjectivity text
		texblob_quote = TextBlob(all_quotes)
		subjectivity_score_quote = texblob_quote.sentiment.subjectivity

		#Get Quote and tokenize it with lowercase letters
		tokenized_quote = wpt().tokenize(all_quotes)
		tokenized_quote = [word.lower() for word in tokenized_quote]

		#Create List of all negative and positive words found in the quote
		positive_words_quote = [word for word in tokenized_quote if word in positive_words]
		negative_words_quote = [word for word in tokenized_quote if word in negative_words]

		#Calculate sentiment score for the quote
		if len(positive_words_quote) == 0 and len(negative_words_quote) == 0:
			sentiment_score_quote = 0
		else:
			sentiment_score_quote = (len(positive_words_quote) + (-len(negative_words_quote)))/(len(positive_words_quote) + len(negative_words_quote))

		#Add Values to list for Output
		#Add Values to list for Output
		if Dataset.iloc[o]["StoreID"] in StoreID_list:
			print("Already saved")
		else:
			Quote_list.insert(0, Dataset.iloc[o]["Quote"])
			sentiment_list_quote.insert(0, sentiment_score_quote)
			positive_words_list_quote.insert(0, len(positive_words_quote))
			negative_words_list_quote.insert(0, len(negative_words_quote))
			StoreID_list.insert(0, Dataset.iloc[o]["StoreID"])
			Academic_ID_list.insert(0, Dataset.iloc[o]["Academic_ID"])
			pysent_quote_scores.insert(0, pysent_score_quote)
			subjectivity_list_quote.insert(0, subjectivity_score_quote)

	else:

		#pysentiment module
		tokens_quote = hiv4.tokenize(Dataset.iloc[o]["Quote"])
		pysent_score_quote = hiv4.get_score(tokens_text)

		#Subjectivity text
		texblob_quote = TextBlob(Dataset.iloc[o]["Quote"])
		subjectivity_score_quote = texblob_quote.sentiment.subjectivity

		#Get Quote and tokenize it with lowercase letters
		tokenized_quote = wpt().tokenize(Dataset.iloc[o]["Quote"])
		tokenized_quote = [word.lower() for word in tokenized_quote]

		#Create List of all negative and positive words found in the quote
		positive_words_quote = [word for word in tokenized_quote if word in positive_words]
		negative_words_quote = [word for word in tokenized_quote if word in negative_words]

		#Calculate sentiment score for the quote
		if len(positive_words_quote) == 0 and len(negative_words_quote) == 0:
			sentiment_score_quote = 0
		else:
			sentiment_score_quote = (len(positive_words_quote) + (-len(negative_words_quote)))/(len(positive_words_quote) + len(negative_words_quote))

		#Add Values to list for Output
		if Dataset.iloc[o]["StoreID"] in StoreID_list:
			print("Already saved")
		else:
			Quote_list.insert(0, Dataset.iloc[o]["Quote"])
			sentiment_list_quote.insert(0, sentiment_score_quote)
			positive_words_list_quote.insert(0, len(positive_words_quote))
			negative_words_list_quote.insert(0, len(negative_words_quote))
			StoreID_list.insert(0, Dataset.iloc[o]["StoreID"])
			Academic_ID_list.insert(0, Dataset.iloc[o]["Academic_ID"])
			pysent_quote_scores.insert(0, pysent_score_quote)
			subjectivity_list_quote.insert(0, subjectivity_score_quote)



#Create Output Dataset

Output["Academic_ID"] = Academic_ID_list
Output["StoreID"] = StoreID_list
#Output["Quote_Sentiment_Pysent"] = pysent_quote_scores
#Output["Full_Text_Sentiment_Pysent"] = pysent_text_scores
Output["Quote_Sentiment_LM"] = sentiment_list_quote
Output["Full_Text_Sentiment_LM"] = sentiment_list_FT
Output["Quote_Positive_Words_LM"] = positive_words_list_quote
Output["Quote_Negative_Words_LM"] = negative_words_list_quote
Output["Full_Text_Positive_Words_LM"] = positive_words_list_FT
Output["Full_Text_Negative_Words_LM"] = negative_words_list_FT
Output["Quote_Subjectivity_TextBlob"] = subjectivity_list_quote
Output["Full_Text_Subjectivity_TextBlob"] = subjectivity_list_FT
Output["Quote"] = Quote_list
Output["Full_Text"] = Full_Text_list



print(Output)
today = date.today()

Output.to_csv("Sentiment_" + str(today.strftime("%b-%d-%Y")) + ".csv")
Output.to_excel("Sentiment_" + str(today.strftime("%b-%d-%Y")) + ".xlsx")
"""

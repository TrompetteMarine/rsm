import pandas as pd
import nltk

from nltk.corpus import sentiwordnet as swn
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import WordPunctTokenizer as wpt

from classes.score import score as Score

import pysentiment as ps
hiv4 = ps.HIV4()

sentiment_dataframe = pd.read_csv("LoughranMcDonald_MasterDictionary_2018.csv")
nltk.download('punkt')
nltk.download('stopwords')
#Filter out only positive and negative words
positive_DF = sentiment_dataframe[sentiment_dataframe["Positive"]>0]
negative_DF = sentiment_dataframe[sentiment_dataframe["Negative"]>0]

#Convert the dataframes to lists and make them lowercase
positive_words = positive_DF["Word"].to_list()
positive_words = [word.lower() for word in positive_words]

negative_words = negative_DF["Word"].to_list()
negative_words = [word.lower() for word in negative_words]

#input list of words
def analyze(wordList) :

	score = Score(0,0)

	for word in wordList:
		if word.lower() in positive_words:
			print("Positive word Found in list: ", word)
			score.positive +=1

		elif word.lower() in negative_words:
			print("Negative word Found in list: ", word)
			score.negative +=1

	return score

def tokenize(extractedText):

	wordList = hiv4.tokenize(extractedText)
	return wordList
import xml.etree.ElementTree as ET
import math
import time
import numpy as np
import pandas as pd
import re
import os
import tensorflow_hub as hub
import spacy
nlp = spacy.load('en_core_web_lg')
#Lemmitization
import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

punctuations="?:!.,;"

#from strsimpy.normalized_levenshtein import NormalizedLevenshtein
#normalized_levenshtein = NormalizedLevenshtein()

#Get dataset
Dataset = pd.read_csv("Text_Data/BuybackOutput.csv")
Quotes_list = []
Full_Texts_list = []
Similarity_list = []


Quotes_num = len(Dataset.index)

Output = pd.DataFrame()


global Lemmitized_Words_List

def Lemmitization_Func(input_text):
	text_words = nltk.word_tokenize(input_text)
	global Lemmitized_Words_List
	Lemmitized_Words_List = []

	#remove stopwords
	tokens_without_sw = [word for word in text_words if not word in stopwords.words()]

	#print(tokens_without_sw)

	#remove punctuation from the texts
	for word in tokens_without_sw:
  		if word in punctuations:
  			tokens_without_sw.remove(word)

	#lemmatize words / word stemming
	for word in tokens_without_sw:
		Lemmitized_Words_List.insert(0, wordnet_lemmatizer.lemmatize(word, pos="v"))
		#print (wordnet_lemmatizer.lemmatize(word, pos="v"))



#Get text and send it to through lemmitization and clean up. Afterwards compare language similiarity with spacy
t = 0 
while t < Quotes_num:
	#Lemmititze Quote and put it back together into 1 string
	Lemmitization_Func(Dataset.iloc[t]["Quote"])
	Lemmitized_Quote = ""
	Lemmitized_Text = ""
	for w in Lemmitized_Words_List:
		Lemmitized_Quote = Lemmitized_Quote + " " + w
	
	#Lemmititze text and put it back together into 1 string
	Edit_Full_Text = Dataset.iloc[t]["Full_Text"]
	Edit_Full_Text = re.sub(Dataset.iloc[t]["Quote"], '', Edit_Full_Text)
	Lemmitization_Func(Edit_Full_Text)
	for w in Lemmitized_Words_List:
		Lemmitized_Text = Lemmitized_Text + " " + w
	
	text_spacy = nlp(Lemmitized_Text)
	quote_spacy = nlp(Lemmitized_Quote)

	print(text_spacy.similarity(quote_spacy))

	#Add Values to Output dataframe
	Similarity_list.insert(0, text_spacy.similarity(quote_spacy))
	Quotes_list.insert(0,Dataset.iloc[t]["Quote"])
	Full_Texts_list.insert(0,Dataset.iloc[t]["Full_Text"])
	#print(Lemmitized_Quote)
	#print("-------------------------BREAK-------------------------")
	#print(Lemmitized_Text)

	t = t+1


#Add Values to Output dataframe
Output["Similarity"] = Similarity_list
Output["Quote"] = Quotes_list
Output["Full_Text"] = Full_Texts_list

#Export Output dataframe
Output.to_csv("Language_Similarity.csv")


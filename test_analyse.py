import unittest

import pandas as pd
from classes.score import score as Score
from analyze import analyze

class TestAnalyse(unittest.TestCase):

    def testScore(self):
        dataset = pd.read_csv("test2.csv",usecols=[0]) 

        sentence = dataset.iloc[:,0]

        #convert to list for performances purpose
        wordList =  sentence.values.tolist()

        score = analyze(wordList)

        self.assertTrue(score.positive >=1) 
        self.assertTrue(score.negative >=1)

if __name__ == '__main__':
    unittest.main()
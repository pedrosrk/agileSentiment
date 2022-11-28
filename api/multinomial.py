from pathlib import Path
import os
import pandas as pd
import nltk
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
import unittest

class dataAnalysis():
    def __init__(self, 
                generalData = os.path.join(Path(__file__).parent.parent, 'database', 'Tweets_Mg.csv'),
                classData = os.path.join(Path(__file__).parent.parent, 'database', 'tweets_classificados_por_forest.csv')): 
        self._generalData = generalData
        self._classData = classData
    
    # getter method
    def get_generalData(self):
        return self._generalData
    
    def get_classData(self):
        return self._classData
      
    # setter method
    def set_generalData(self, x):
        self._generalData = x
    
    def set_classData(self, x):
        self._classData = x

    def __del__(self):
        pass

    def demoAnalysis(self):
        data = dataAnalysis()
        dataset = pd.read_csv(data.get_generalData(), encoding='utf-8')
        tweets = dataset["Text"].values
        classes = dataset["Classificacao"].values
        vectorizer = CountVectorizer(analyzer = "word")
        freq_tweets = vectorizer.fit_transform(tweets)
        modelo = MultinomialNB()
        modelo.fit(freq_tweets, classes)

        dataTest = pd.read_csv(data.get_classData(),encoding='utf-8')
        testes = dataTest["texto"].values
        classesTest = dataTest["sentimento"].values
        
        freq_testes = vectorizer.transform(testes)
        result = modelo.predict(freq_testes)

        return metrics.accuracy_score(classesTest, result)

if __name__ == '__main__':
    data = dataAnalysis()
    print(data.demoAnalysis())
from __future__ import print_function, division
#from future.utils import iteritems
#from builtins import range
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
#from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
#from sklearn.svm import SVC
from wordcloud import WordCloud
#from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('/home/adventum/Downloads/spam.csv',encoding='ISO-8859-1') # use pandas for convenience

#data = data.drop(["Unnamed: 2","Unnamed: 3","Unnamed: 4"],axis=1)

data.columns = ['labels','data']

data['b_labels'] = data['labels'].map({'ham': 0, 'spam': 1})
Y = data['labels']

countVectorizer = CountVectorizer(decode_error='ignore')
X = countVectorizer.fit_transform(data['data'])

data2 = ['get loan for free','Get 7 Days holiday for 25Yrs And 3N/4D Europe Cruise','MASSIVE DEALS on Mobiles! #BigShoppingDays','win $1000 for free']
df = pd.DataFrame(data2, columns = ['data'])
Z = countVectorizer.transform(df['data'])

'''
#tfidf
tfidf = TfidfVectorizer(decode_error='ignore')
X = tfidf.fit_transform(data['data'])
'''
#Xtrain, Xtest, Ytrain, Ytest = train_test_split(X,Y,test_size = 0.33)

model = MultinomialNB()
#model = KNeighborsClassifier(n_neighbors=2)
#model = SVC(kernel='linear')
model.fit(X, Y)


predictions = model.predict(Z)
#print(predictions)
#print("train score:", model.score(Xtrain, Ytrain))
#print("test score:", model.score(Xtest, Ytest))

# visualize the data
def visualize(label):
  words = ''
  for msg in data[data['labels'] == label]['data']:
    msg = msg.lower()
    words += msg + ' '
  wordcloud = WordCloud(width=600, height=500).generate(words)
  plt.imshow(wordcloud)
  plt.axis('off')
  plt.show()

visualize('spam')
visualize('ham')

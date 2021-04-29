#import and inspect a .csv dataset
import pandas as pd
music_data = pd.read_csv('music.csv')
music_data

#prepare the data
#1. separate columns in INPUT and OUTPUT category
#2. drop the GENRE column to get the INPUT dataset (X)
#3. create the OUTPUT dataset (y), that contains only the GENRE column
X = music_data.drop(columns=['genre'])
X
y = music_data['genre']
y

#create a model 
#Model used: Decision tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X, y)

#get the output predictions
predictions = model.predict([ [21, 1], [22, 0] ])
predictions
#calculate the accuracy of a model
#1. split the dataset into two groups: TRAINING and TESTING. For TESTING, give it around 20% of size.
#2. change the predictions call (commented above)
#3. calculate the accuracy score of a model with this dataset (from 0.0 to 1.0).
#note: this dataset contains a small number of data, that is why the SCORE is changing every time the script is run.
#In the real world dataset, there are much more data, so it is more accurate. 
#In the real world problem, if the SCORE is low (below 0.5 - 50%), that means you should consider to go with some ...
#other model (algorithm) or improve currently used algorithm.
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
predictions
accuracy_score(y_test, predictions)
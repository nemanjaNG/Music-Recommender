#You don't have to train a model every time.
#Instead, you can save a model as a binary file using the 'joblib' set of tools, ...
#and load it. Then, you can get the output predictions based on the given input.
import joblib as jl
model = jl.load('music-recommender.joblib')
predictions = model.predict([ [21, 1] ])
predictions

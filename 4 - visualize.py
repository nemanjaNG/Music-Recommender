#create a .dot file that can give a visual representation of a desicion tree
from sklearn import tree
import joblib as jl

model = jl.load('music-recommender.joblib')
tree.export_graphviz(model, out_file='music-recommender.dot',
                   feature_names=['age', 'gender'],
                   class_names=sorted(y.unique()),
                    label='all',
                    rounded=True,
                    filled=True)
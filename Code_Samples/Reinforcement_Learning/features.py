__author__ = 's1674939'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Imports data from csv file
path = "/afs/inf.ed.ac.uk/user/s16/s1674939/rl-cw2/fa_out.csv"
fa_df = pd.read_csv(path, delimiter = ',')

weight =[]

items = fa_df['Weights'][0].split(" ", 1)
for x in items:
    if x != "" and x != '[':
        weight.append(x)

weight1 = [i.split(' ')[1]  for i in weight]
weight2 = [i.split(' ')[4]  for i in weight]
weight3 = [i.split(' ')[7]  for i in weight]
weight4 = [i.split(' ')[9]  for i in weight]
weight5 = [i.split(' ')[11]  for i in weight]
weight6 = [i.split(' ')[14]  for i in weight]
weight7 = [i.split(' ')[16]  for i in weight]
weight8 = [i.split(' ')[18]  for i in weight]
weight9 = [i.split(' ')[21]  for i in weight]
weight10 = [i.split(' ')[24]  for i in weight]

weights = (weight1, weight2, weight3, weight4, weight5, weight6, weight7, weight8, weight9, weight10)

feature = ", ".join([item for sublist in weights for item in sublist])

feat1 = float(feature.split(',')[0])
feat2 = float(feature.split(',')[1])
feat3 = float(feature.split(',')[2])
feat4 = float(feature.split(',')[3])
feat5 = float(feature.split(',')[4])
feat6 = float(feature.split(',')[5])
feat7 = float(feature.split(',')[6])
feat8 = float(feature.split(',')[7])
feat9 = float(feature.split(',')[8])
feat10 = feature.split(',')[9]
# Used to take the ']' off the end of feat10
feat11 = float(feat10[0:5])

features = (feat1, feat2, feat3, feat4, feat5, feat6, feat7, feat8, feat9, feat11)


n_feat = 10
index = np.arange(n_feat)
error = {'ecolor': '0.3'}
fig, ax = plt.subplots()

features = plt.bar(index, features, error_kw = error)

plt.xlabel('Feature')
plt.ylabel('Accuracy')
plt.title('Function Approximation Feature Weights')
plt.xticks(index + 0.4,('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10'))

plt.tight_layout()
plt.show()


__author__ = 's1674939'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Imports data from Function Approximation csv file
path = "/afs/inf.ed.ac.uk/user/s16/s1674939/rl-cw2/fa_out200.csv"
fa_df = pd.read_csv(path, delimiter = ',')

total = fa_df['Total Reward']


fig = plt.figure(figsize =(12,8))
ax = fig.add_subplot(111)
ax.hist(total, bins = 35)


ax.set_title('Function Approximation Total Reward')
ax.set_ylabel('Frequency')
ax.set_xlabel('Reward at Last Iteration')
ax.set_ylim(0,20)
ax.set_xlim(0,40)
plt.show()
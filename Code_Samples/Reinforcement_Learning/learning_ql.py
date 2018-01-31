__author__ = 's1674939'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Import data from Q-learning csv file
path1 = "/afs/inf.ed.ac.uk/user/s16/s1674939/rl-cw2/ql_out3.csv"
ql_df = pd.read_csv(path1, delimiter = ',')


# Total Reward per episode Q-learning Algorithm
total1 = ql_df['Total Reward']

fig1 = plt.figure(figsize = (12,8))
ax1 = fig1.add_subplot(111)
ax1.plot(total1, 'r', label = 'Q-learning')



ax1.set_title('Q-Learning Convergence')
ax1.set_xlabel('Episode')
ax1.set_ylabel('Total Reward')
ax1.set_xlim(0,275)
ax1.set_ylim(0,100)

plt.show()
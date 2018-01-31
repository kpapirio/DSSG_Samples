__author__ = 's1674939'
import pandas as pd
import matplotlib.pyplot as plt

#Imports data from Function Approximation csv file
path = "/afs/inf.ed.ac.uk/user/s16/s1674939/rl-cw2/fa_out200.csv"
fa_df = pd.read_csv(path, delimiter = ',')


#Total Reward per episode Funtion Approximation Agent
total = fa_df['Total Reward']

fig = plt.figure(figsize =(12,8))
ax = fig.add_subplot(111)
ax.plot(total, label = 'Function Approximation')

ax.set_title('Function Approximation Convergence')
ax.set_xlabel('Episode')
ax.set_ylabel('Total Reward')

plt.show()

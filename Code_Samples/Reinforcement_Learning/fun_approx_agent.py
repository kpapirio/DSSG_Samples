import cv2
import csv
import numpy as np
import random

from enduro.agent import Agent
from enduro.action import Action


class FunctionApproximationAgent(Agent):
    def __init__(self):
        super(FunctionApproximationAgent, self).__init__()

        # Initialize state variables
        self.new_state = []
        self.last_state = []

        # Intialize action variables
        self.prev_action = 0

        # Learning rate
        self.lr = 0.00001
        # Discounting factor
        self.gamma = 0.9
        # Exploration rate
        self.epsilon = 0.01

        # Initialize reward variables
        self.tot_reward = 0
        self.cur_reward = 0

        # Initialize weight vector based on number of attributes
        self.phi = np.zeros(10)

        self.idx = {i: a for i, a in enumerate(self.getActionsSet())}

        self.data = [[]]


    def initialise(self, road, cars, speed, grid):
        ''' Called at the beginning of an episode. Use it to construct
         the initial state. '''

        # Reset the total reward for the episode and intitialize state
        self.new_state = [road, cars, speed, grid]
        self.tot_reward = 0

    def feature(self, a, state):
        ''' Defines features corresponding to behavior requirements'''

        road, cars, speed, grid = state

        i = np.argmax(grid[0])

        # Feature 1: Agent accelerating and car in front
        feat1 = (a == Action.ACCELERATE and np.sum(grid[:4,i]) > 0)

        # Feature 2: Agent not accelerating and no car in front
        feat2 = (a != Action.ACCELERATE and np.sum(grid[:4,i]) == 0)

         # Feature 3: Agent is accelerating and speed is greater than or equal to 25
        feat3 = (a == Action.ACCELERATE and speed >= 25 )

        # Feature 4: Agent is not accelerating and speed is less than 25
        feat4 = (a != Action.ACCELERATE and speed < 25)

        # Feature 5: Agent is not accelerating and speed is less than 25
        feat5 = (a == Action.ACCELERATE and speed < 25)

        # Feature 6: Agent is accelerating
        feat6 = (a == Action.ACCELERATE)

        #Feature 7: Agent moves right
        feat7 = (a == Action.RIGHT)

        #Feature 8: Agent moves left
        feat8 = (a == Action.LEFT)

        # Feature 9: Agent move right and car ahead to the right
        feat9 = (a == Action.RIGHT and np.sum(grid[0:4, i:i+2]) == 1)

        # Feature 10: Agent moves left and car ahead and to the left
        feat10 = (a == Action.LEFT and np.sum(grid[0:4, i-1:i+1]) == 1)

        return np.array([feat1, feat2, feat3, feat4, feat5, feat6, feat7, feat8, feat9, feat10])

    def act(self):
        '''Implements the decision making process for selecting
       an action. Remember to store the obtained reward.'''

        # If Exploring select random action
        if np.random.uniform(0., 1.) < self.epsilon:
            rand = random.randint(1, 4)
            if (rand == 1):
                self.prev_action = Action.LEFT
            if (rand == 2):
                self.prev_action = Action.RIGHT
            if (rand == 3):
                self.prev_action = Action.ACCELERATE
            if (rand == 4):
                self.prev_action = Action.BRAKE
        else:
            Q_func = [self.feature(a, self.new_state).dot(self.phi) for a in self.getActionsSet()]
            self.prev_action = np.random.choice(np.where(Q_func == max(Q_func))[0])
            self.prev_action = self.idx[self.prev_action]

        # Update Reward
        self.cur_reward = self.move(self.prev_action)
        self.tot_reward += self.cur_reward

    def sense(self, road, cars, speed, grid):
        ''' Constructs the next state from sensory signals '''

        self.last_state = self.new_state
        self.new_state = [road, cars, speed, grid]

    def learn(self):
        ''' Performs the learning procedure.
        It is called after act() and sense() so you have access to the latest tuple (s, s', a, r).'''

        Q_func_max = max([self.feature(a, self.new_state).dot(self.phi) for a in self.getActionsSet()])
        last = self.feature(self.prev_action, self.last_state)
        last_Q_func_max = last.dot(self.phi)

        self.phi += (self.lr * (self.cur_reward + self.gamma * Q_func_max - last_Q_func_max) * last)

    def callback(self, learn, episode, iteration):
        '''Called at the end of each timestep for reporting/debugging purposes.'''
        if not iteration % 100:
            print "{0}/{1}: {2}".format(episode, iteration, self.tot_reward)

        self.lr *= 0.99995

        # You could comment this out in order to speed up iterations
        cv2.imshow("Enduro", self._image)

        if iteration == 6500:
            self.data += [[episode, self.tot_reward, self.phi]]

        cv2.waitKey(1)

if __name__ == "__main__":
    a = FunctionApproximationAgent()
    a.run(True, episodes=200, draw=True)
    print 'Total reward: ' + str(a.tot_reward)

    #Export to csv file
    path =  "/afs/inf.ed.ac.uk/user/s16/s1674939/rl-cw2/fa_out200.csv"
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in a.data:
            print line
            writer.writerow(line)
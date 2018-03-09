# Reinforcement Learning: Overview

This RL project involved playing the Enduro game within the ALE environment and had two main goals. 

1. The design and implementation of a Q-learning based agent that modeled the environment (passing cars, avoiding collisions).

Results were compared against a baseline random agent, and manipulations of the time horizon showed how the agent’s awareness of state-space dimensionality affects performance and reward anticipation. 

2. The design and implementation of an agent based on a linear approximation state-action value function with feature vectors based on the sensing capabilities, and an off-policy TD update rule.

The resulting learning curves were compared against the original Q-learning algorithm, as well as the convergence rates of each FA model. A visualization of the weights associated with each feature was performed to inspect usefulness. 



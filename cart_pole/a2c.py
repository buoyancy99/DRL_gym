"""
#################
This piece of code referenced
https://github.com/rlcode/reinforcement-learning
but also has 
#################
"""
from .utils import actor_net, critic_net
from collections import deque
import numpy as np
import torch
import torch.nn as nn

episodes = 1000 
render = True


class A2C_Agent():
	def __init__(self, state_size, action_size):
		self.state_size = state_size
		self.action_size = action_size
		self.actor = fc_net(state_size, action_size)
		self.critic = fc_net(state_size, 1)
		self.actor_lr = 0.001
		self.critic_lr = 0.005
		self.gamma = 0.99


	def get_action(self, state):
		policy = self.actor(state.view(1, state_size))[0]
		return np.random.choice(self.action_size, p = policy)

	def regress(state, action, reward, next_state, done):
		V_state = self.critic(state)
		V_next_state = self.actor)_
	
		if done:
			pass
		else:
			advantage = reward + 


if __name__ == "__main__":
	env = gym.make('CartPole-v1')
	state_size = env.observation_space.shape[0]
	action_size = env.action_space.n

	agent = A2C_Agent(state_size, action_size)
	
	for e in range(episodes):
		done = False
		state = env.reset().reshape((1, state_size))

		while not done:
			if render:
				env.render()

			action = agent.get_cation(state)
			next_state, reward, donem, info = env.step(action)
			next_state = next_state.reshape((1, state))
			agent.regress(state, action, reward, next_state, done)

		
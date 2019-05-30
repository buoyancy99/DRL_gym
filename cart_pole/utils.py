import torch.nn as nn

class fc_net(nn.Module):
	def __init__(self, in_C, out_C):
		super(fc_net, self).__init__()
		self.layers = nn.Sequential(
			nn.Linear(in_C, 32),
			nn.ReLU(),
			nn.Linear(32, out_C)
		)

	def forward(self, X):
		return self.layers(X)

class actor_net(nn.Module):
	def __init__(self, in_C, out_C):
		super(actor_net, self).__init__()
		self.layers = nn.Sequential(
			nn.Linear(in_C, 32),
			nn.ReLU(),
			nn.Linear(32, out_C)
			nn.Softmax()
		)

	def forward(self, X):
		return self.layers(X)


class critic_net(nn.Module):
	def __init__(self, in_C, out_C):
		super(critic_net, self).__init__()
		self.layers = nn.Sequential(
			nn.Linear(in_C, 32),
			nn.ReLU(),
			nn.Linear(32, out_C)
		)

	def forward(self, X):
		return self.layers(X)
import numpy as np
np.random.seed(0)  #generating same number

X = [[0.1, 0.2, 0.3, 0.4 ],
     [1, 2, 3, 4],
     [-0.8, 0.6, -0.5, 0.2] ]

class layer_dense:
	def __init__ (self, n_input, n_neuron ):
		self.weights = 0.10*np.random.randn(n_input, n_neuron)
	def forward(self):
		pass




print(np.random.randn(4, 3))
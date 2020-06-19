input = [1.1, 1.2, 1.3, 1.4] #INPUT

weight = [ [2.1, 2.2, 2.3, 2.4],
         [3.1, 3.2, -3.3, 3.4],
         [4.1, -40.2, 04.3, 4.4] ]

biases = [1.6, 2, 3]


'''

layer_outputs = [] #output of current layer

for neuron_weights, neuron_biases in zip(weight, biases):
	neuron_output = 0 #output of givin neuron
	for n_input, weight in zip(input, neuron_weights):
		neuron_output+= n_input*weight
	neuron_output+= neuron_biases	
	layer_outputs.append(neuron_output)
print(layer_outputs)
'''
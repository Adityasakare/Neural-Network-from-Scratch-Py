import numpy as np
inputs = [1.0, 1.1, 1.2, 1.3]

weights = [ [2.1, 2.2, 2.3, 2.4],
         [3.1, 3.2, -3.3, 3.4],
         [4.1, -40.2, 04.3, 4.4] ]

biases = [1.6, 2, 3]

output = np.dot(weights, inputs) + biases
print(output)
import numpy as np

layer_output = np.array((0.2,0.5,1.3,0.8,1.1))
test = np.random.randint(0,high=2,size=layer_output.shape)
print(test)
layer_output *= np.random.randint(0,high=2,size=layer_output.shape)

print(layer_output)
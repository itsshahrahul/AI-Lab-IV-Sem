import numpy as np
import matplotlib.pyplot as plt

# define the sigmoid function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# define the derivative of sigmoid function
def sigmoid_derivative(x):
    return x*(1-x)

# input dataset
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
# output dataset
outputs = np.array([[0],[1],[1],[0]])

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
weights0 = 2*np.random.random((2,2)) - 1
weights1 = 2*np.random.random((2,1)) - 1

# learning rate
alpha = 0.1

# number of iterations
num_iterations = 10000

# store the error
error = []

for i in range(num_iterations):
    # forward propagation
    layer0 = inputs
    layer1 = sigmoid(np.dot(layer0, weights0))
    layer2 = sigmoid(np.dot(layer1, weights1))

    # calculate the error
    layer2_error = outputs - layer2
    error.append(np.mean(np.abs(layer2_error)))

    # back propagation
    layer2_delta = layer2_error*sigmoid_derivative(layer2)
    layer1_error = layer2_delta.dot(weights1.T)
    layer1_delta = layer1_error*sigmoid_derivative(layer1)

    # update the weights
    weights1 += layer1.T.dot(layer2_delta)*alpha
    weights0 += layer0.T.dot(layer1_delta)*alpha

plt.plot(error)
plt.xlabel('Training')
plt.ylabel('Error')
plt.show()
print('Output after training')
print(layer2)
print('Weights after training')
print(weights0)
print(weights1)

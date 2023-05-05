import numpy as np
import random
import utils


class NeuralNetwork:
    def __init__(self, architecture):
        self.architecture = architecture
        self.weights = []
        self.biases = []
        self.init_weights()
        self.init_biases()

    @utils.try_catch
    def init_weights(self):
        for i in range(1, len(self.architecture)):
            self.weights.append(np.random.randn(self.architecture[i], self.architecture[i - 1]))

    @utils.try_catch
    def init_biases(self):
        for i in range(1, len(self.architecture)):
            self.biases.append(np.random.randn(self.architecture[i], 1))

    @utils.try_catch
    def feedforward(self, input):
        input = np.array(input)
        input = input.reshape(len(input), 1)
        for i in range(len(self.weights)):
            input = np.dot(self.weights[i], input)
            input += self.biases[i]
            input = self.activation(input)
        return input

    @utils.try_catch
    def activation(self, x):
        # return 1 / (1 + np.exp(-x))
        return np.maximum(0, x)

    @utils.try_catch
    def mutate(self, rate):
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    if random.random() < rate:
                        self.weights[i][j][k] += random.uniform(-1, 1)
        for i in range(len(self.biases)):
            for j in range(len(self.biases[i])):
                if random.random() < rate:
                    self.biases[i][j] += random.uniform(-1, 1)

    @utils.try_catch
    def breed(self, other, rate=0.5):
        child = NeuralNetwork(self.architecture)
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    if random.random() < rate:
                        child.weights[i][j][k] = self.weights[i][j][k]
                    else:
                        child.weights[i][j][k] = other.weights[i][j][k]
        for i in range(len(self.biases)):
            for j in range(len(self.biases[i])):
                if random.random() < rate:
                    child.biases[i][j] = self.biases[i][j]
                else:
                    child.biases[i][j] = other.biases[i][j]
        return child

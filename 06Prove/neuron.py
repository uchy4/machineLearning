import random as rd
import numpy as np
import math as m
import csv
from sklearn import preprocessing as pr

class Neuron(object):
    def __init__(self,length, learn = 10):
        self.weights = [rd.uniform(-1,1) for x in range(length)]
        self.learn = learn #default learning rate
        self.changed = False
        self.output = 0

    #update the weights
    def update(self):
        newWeights = []
        for x,w in zip(self.values,self.weights):
            newWeights.append(w-self.learn*(self.pred-self.weights[0])*x)
        self.weights = newWeights
        self.changed = True

    #total of the weights * inputs
    def calcSum(self, inputs):
        output = 0
        for x,w in zip(inputs,self.weights):
            output+=x*w
        self.output = output
        return output

    #calc activation
    def activation(self):
        # s's algorithm
        return 1/(1+np.exp(-self.output))
 





            

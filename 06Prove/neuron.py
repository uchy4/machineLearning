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
        self.sum = 0

    #total of the weights * inputs
    def calcSum(self, inputs):
        output = 0
        for x,w in zip(inputs,self.weights):
            output+=x*w
        self.sum = output
        return output

    #calc activation //sigmoid 1st derivative
    def activation(self):
        # s's algorithm
        a = 1/(1+np.exp(-self.sum))
        self.actv = a
        return a
 





            

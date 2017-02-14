import random as rd
import numpy as np
import math as m
import csv
from sklearn import preprocessing as pr
import neuron

class Network(object):

    def __init__(self, length, numLayers, nodeCounts):
        temp = [length]+nodeCounts
        #initializing the layers with specified amount of nodes per layer
        self.layers = [[neuron.Neuron(temp[i+1]) for n in range(nodeCounts[i])] for i in range(numLayers)]
        self.pred = 0
        self.arr = []

    #recursive : gets the activation and passes it on to the next level
    def calcLayer(self, inputs, layerNum=0):
        newInputs = [-1]
        for n in self.layers[layerNum]:
            h = n.calcSum(inputs)
            a = n.activation()
            newInputs.append(a)

        layerNum+=1

        #quit out if you hit the output layer
        if layerNum == len(self.layers):
            #for calculating prediction
            self.pred = newInputs[1:].index(max(newInputs[1:]))
            self.arr = newInputs[1:]
            return
        else:
            self.calcLayer(newInputs, layerNum)





#getting data and user preferences
data = csv.CSV().data
numLayers = int(raw_input('how many layers?: '))
nodeCounts = []
for x in range(numLayers):
    if x==numLayers-1:
        nodeCounts.append(int(raw_input('nodes for output layer: ')))
    else:
        nodeCounts.append(int(raw_input('nodes for hidden layer ' + str(x+1) + ': '))) 

#initializing neural network
n = Network(len(data[0]),numLayers, nodeCounts)
predictions = []
for row in data:
    n.calcLayer(row[:-1])
    predictions.append((n.pred, n.arr))

#printing accuracy
accuracy = 0
total = len(data)
for p,d in zip(predictions,data):
    print p, int(d[-1])
    if p[0]==int(d[-1]):
        accuracy+=1 
print 100*float(accuracy)/float(total),'%'






    
    

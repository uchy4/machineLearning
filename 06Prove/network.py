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
        self.target = 0
        self.errorList = []

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
            self.pred = newInputs[1:].index(max(newInputs[1:]))#omit the bias node

            #activation of output layer calculates error
            self.arr = newInputs[1:]
            return
        else:
            self.calcLayer(newInputs, layerNum)


    def calcError(self):

        errorList = []
        count = 0
        for layer in reversed(self.layers): #bias nodes need the weights changes
        #calc hidden layer
            errors = []
            if count == 0:
                for l in layer:
                    error = l.actv*(1 - l.actv)*(l.actv - self.target) #output layer error
                    errors.append(error)
            else:
                for l in layer:
                    sumW = 0
                    for w,e in zip(l.weights,errorList[-1]):
                        sumW += (w*e)
                    error = l.actv*(1 - l.actv)*sumW
                    errors.append(error)
            count+=1
            errorList.append(errors)
        self.errorList = reversed(errorList)
                            
        #calc ouput layer
            


    def modWeights(self):

        for layer in self.layers:
            for l,error in zip(layer,self.errorList):
                newWeights = []
                #print l.weights
                for w,e in zip(l.weights,error):
                    new = w -(l.learn * e * l.actv)
                    newWeights.append(new)
                l.weights = newWeights
                #print l.weights
                    
                    





#getting data and user preferences
data = csv.CSV().data[:10]
np.seterr(all='ignore')
numLayers = int(raw_input('how many hidden layers?: '))+1
nodeCounts = []
for x in range(numLayers):
    if x==numLayers-1:
        nodeCounts.append(int(raw_input('how many targets: ')))
    else:
        nodeCounts.append(int(raw_input('nodes for hidden layer ' + str(x+1) + ': '))+1)#add 1 for bias


########################

#initializing neural network
n = Network(len(data[0]),numLayers, nodeCounts)
predictions = []

for i in range(10000):
    for row in data:
        n.target = row[-1]
        n.calcLayer([-1] + row[:-1])#omit the target answer
        n.calcError()
        n.modWeights()
        if i == 9999:
            predictions.append((n.pred, n.arr))



########################

#printing accuracy
accuracy = 0
total = len(data)
for p,d in zip(predictions,data):
    print p, int(d[-1])
    if p[0]==int(d[-1]):
        accuracy+=1 
print 100*float(accuracy)/float(total),'%'






    
    

from __future__ import division
from sklearn import datasets
from sklearn.cross_validation import train_test_split as tts
import random
import numpy as np

import csv

##NOTE: highest entropy is the feature with the most variety

class DecisionTree(object):

    def __init__(self, datafile, indexFirst=False):
        #initializing
        self.indexFirst = indexFirst
        self.percent = 0
        self.data = datafile
        self.targetEntropy = 0
        self.bestEntropy = 0
        self.fEntropies = []
        self.indexes = ()
        

    def fit(self):
        #use this data to come up with an algorithm
        pass

    def predict(self,k):
        #use this data to set the test results
        pass

    #entropy of whole set minus entropy of particular feature
    #wE - pE = answerE
    def calcEntropy(self,p):
        if p != 0:
            return -p *np.log2(p)
        else:
            return 0

    def getSet(self, index):

        targets = []

        for row in self.data:
            targets.append(row[index])

        return list(set(targets)), targets


    def getEntropy(self,index,tIndex):
        targets, targetList = self.getSet(tIndex)
        check, feature = self.getSet(index)
        entropies = []

        for c in check:
            weighted = 0
            count = np.zeros(len(targets))
            for i in range(len(feature)):
                if c == feature[i]:
                    count[targets.index(targetList[i])]+=1
            entropy = 0
            for x in count:
                entropy+=self.calcEntropy(x/sum(count))
            
            weighted += entropy* sum(count)/len(feature)
            entropies.append(weighted)

        return sum(entropies)

    def start(self):

        tIndex = len(self.data[0])-1         #undetermined
        fIndex =  [i for i in range(len(self.data[0]))] #undetermined
        
        if self.indexFirst:
            tIndex = 0
        fIndex.remove(tIndex)

        self.indexes = (tIndex,fIndex)
        
        fEntropies = []

        temp = self.getEntropy(tIndex,tIndex)
        self.targetEntropy = temp

        for f in fIndex:
            self.fEntropies.append(self.getEntropy(f,tIndex))

        self.bestEntropy = self.fEntropies.index(min(self.fEntropies))

    def compare(self):
        #iterate trough the arrays and compare test results
        percent = 0.0
        for x in range(len(self.t_test)):
            if self.pred[x] == self.t_test[x]:
                percent+=1
        percent = 100*(percent/len(self.t_test))
        self.percent = round(percent,2)
            

    def display(self):
        print 'Tree: '

###############################

def show(d):
    for v in d.data:
        print v
    print '\ntarget index: ' + str(d.indexes[0])
    print 'feature indexes: ' + str(d.indexes[1])
    print '\nEntropies for each feature:'
    for x in d.fEntropies:
        print x
    print '\nLowest Entropy:\n' + str(d.bestEntropy)
    
###############################
    
def prompt():
    fileName = {'1':('parties.txt',False,True),
            '2':('iris.txt',False,False),
            '3':('lenses.txt',True,False),
            '4':('credit.txt',True,False)}

    for key, value in fileName.iteritems():
        print key + ': ' + value[0]
        
    fIndex = ''
    while not fIndex in fileName:
        fIndex = raw_input('Which file#: ')
        
    return fileName[fIndex]

################################



p = prompt()
d = DecisionTree(csv.CSV(p[0],p[1]).data,p[2])
d.start()
show(d)



################################

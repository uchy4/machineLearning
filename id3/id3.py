from __future__ import division
from sklearn import datasets
from sklearn.cross_validation import train_test_split as tts
import random
import numpy as np
import node

import ctypes

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
        self.nodes = node.Node()
        self.predictions = []
        self.test_data = []
        self.path = []

    def swap(self, count=3):
        random.shuffle(self.data)
        print count
        test_data = []
        fit_data = []
        for x in range(len(self.data)):
            if x%count == 0:
                test_data.append(self.data[x])
            else:
                fit_data.append(self.data[x])

        if len(test_data)==0:
            self.swap()
        self.data = fit_data
        self.test_data = test_data

    def predict(self):
        #use this data to set the test results
        n = self.nodes
        for d in self.test_data:
            try:
                self.predictions.append(self.recurAnswer(d,n))
            except StandardError:
                print 'something is missing'

    def recurAnswer(self,d,n):
##        try:
##            n.children
##        except StandardError:
##            print n
##            return n.parent.answer
        if n.isLeaf:
            return n.answer
        else:
            for a in n.children:
                if d[a.column]== a.type:
                    #print a.column
                    return self.recurAnswer(d,a)
            return n.answer

    #entropy of whole set minus entropy of particular feature
    #wE - pE = answerE
    def calcEntropy(self,p):
        if p != 0:
            return -p *np.log2(p)
        else:
            return 0

    def getSet(self, index, data):

        targets = []

        for row in data:
            targets.append(row[index])

        return list(set(targets)), targets

    def fit(self):

        tIndex = len(self.data[0])-1         #undetermined
        fIndex =  [i for i in range(len(self.data[0]))] #undetermined
        data = self.data
        
        if self.indexFirst:
            tIndex = 0
        fIndex.remove(tIndex)

        self.indexes = (tIndex,fIndex)
        
        fEntropies = []

        data = self.data
        self.nodes = node.Node()
        used = np.zeros(len(data[0])-1)

        self.makeTree(data, self.nodes, used, fIndex, tIndex)

    def bestAttribute(self,data, vIndexes, tIndex, used):
        targets, tColumn = self.getSet(tIndex, data)
        bestAtt = []

        for v in vIndexes:
            check, vColumn = self.getSet(v, data)
            entropies = []
            answer = list(np.zeros(len(targets)))

            for c in check:
                weighted = 0
                count = np.zeros(len(targets))
                entropy = 0

                for type, target in zip(vColumn, tColumn):
                    if c == type:
                        count[targets.index(target)]+=1
                for x in count:
                    entropy+=self.calcEntropy(x/sum(count))
                
                weighted += entropy* sum(count)/len(vColumn)
                entropies.append(weighted)
                for a in range(len(answer)):
                    answer[a] = count[a]
            #print targets[int(answer.index(max(answer)))]
            ans = targets[int(answer.index(max(answer)))]
            bestAtt.append((sum(entropies),(v,check,ans)))
        return min(bestAtt)[1]

    #recursive function to construct tree
    def makeTree(self, data, n, used, fIndex, tIndex):
        column, types, answer = self.bestAttribute(data, fIndex, tIndex, used)
        
        for t in types:
            if len(types)>1:
                newNode = n.grow(node.Node(column, n.level +1, t,answer),n)
                newData = self.cut(data, column, t)
                self.makeTree(newData, newNode,used, fIndex, tIndex)

    def cut(self,data, column, type):
        newData = []
        for d in data:
            if d[column]==type:
                newData.append(d)
        return newData

    def compare(self):
        #iterate trough the arrays and compare test results
        percent = 0.0
        print 'test: ' + str(len(self.test_data))
        print 'pred: ' + str(len(self.predictions))
        for x,y in zip(self.test_data, self.predictions):
            if x[self.indexes[0]] == y:
                percent+=1
        percent = 100*(percent/len(self.test_data))
        self.percent = round(percent,2)
            

    def display(self,n,l=0,h='Lowest',path = 'root'):
        if l:
           l = len(n.children)-1
           h = 'Highest'
        if not n.isLeaf:
            path += '->if(col==' + str(n.column) + ' & type==' + str(n.type) + ')'
            self.display(n.children[l],l,h,path)
        else:
            path += '->ANSWER:' + str(n.answer)
            print '\n' + h + ' entropy path:'
            print path

###############################

def show(d):
    #for v in d.data:
     #   print v
    print '\ntarget index: ' + str(d.indexes[0])
    print 'feature indexes: ' + str(d.indexes[1])
    print '\nEntropies for each feature:'
    print '\naccuracy: ' + str(d.percent)
    
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

def multiply(data, yes):
    if yes:
        newData = []
        for x in range(5):
            for d in data:
                newData.append(d)
        return newData
    return data


p = prompt()
data = csv.CSV(p[0],p[1]).data
data = multiply(data,p[1])
d = DecisionTree(data,p[2])
d.swap()
d.fit()
d.predict()
d.compare()
show(d)
d.display(d.nodes.children[0])
d.display(d.nodes.children[len(d.nodes.children)-1],2)



################################

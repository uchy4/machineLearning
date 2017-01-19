from sklearn import datasets
from sklearn.cross_validation import train_test_split as tts
import random





class Iris(object):

    def __init__(self, filename):
        
        self.file = open(filename, 'r')
        self.names = []
        self.data = []
        
    def line(self):

        for line in self.file:
            self.parseLine(line)
        print self.names
        print self.data
            
    def parseLine(self, line):

        temp = (line.split(',',4))
        temp2 = map(float, temp[:4])
        self.data.append(temp2)
        check = temp[4].replace('Iris-','')
        self.names.append(check.replace('\n',''))
        
iris = Iris('IRIS.txt')
iris.line()

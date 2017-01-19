from sklearn import datasets
from sklearn.cross_validation import train_test_split as tts
import random


class Classifier(object):

    def __init__(self, iris):
        #setting the train and test data and targets
        self.iris = iris
        self.d_train, self.d_test, self.t_train, self.t_test = tts(iris.data, iris.target, train_size=.7, random_state=random.randint(400,600))
        self.percent = 0
        self.distances = []
        self.pred = []

    def fit(self):
        #use this data to come up with an algorithm
        pass

    def predict(self,k):
        #use this data to set the test results
        for t in self.d_test:
            self.distances.append(self.compDist(t,k)) #appends distances

        self.calcPrediction()

    #used by predict()
    def calcPrediction(self):
        
        for d in self.distances:
            results = []
            for index in d:
                results.append(self.t_train[index[1]])
            self.pred.append(self.mostCommon(results))

    #used by predict()
    def mostCommon(self, types):
        check = [0,0,0]
        results = []
        for t in types:
            check[t]+=1
        results.append(check.index(max(check)))

        
        return check.index(max(check))

    #used by predict()
    def compDist(self, item, k):
        distance = []
        for index in range(len(self.d_train)):
            tempDist = 0
            for i in range(len(self.d_train[index])):
                tempDist += ((item[i]-self.d_train[index][i])**2)
            distance.append((tempDist,index))
        distance.sort()
        return distance[:k]

    def compare(self):
        #iterate trough the arrays and compare test results
        percent = 0.0
        for x in range(len(self.t_test)):
            if self.pred[x] == self.t_test[x]:
                percent+=1
        percent = 100*(percent/len(self.t_test))
        self.percent = round(percent,2)
            

    def display(self):
        print 'Accuracy: ' + str(self.percent)+'%'

k = raw_input("how many neightbors?: ")
classifier = Classifier(datasets.load_iris())
classifier.predict(int(k))
classifier.compare()
classifier.display()



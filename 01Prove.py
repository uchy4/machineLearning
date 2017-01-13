from sklearn import datasets
from sklearn.cross_validation import train_test_split as tts
import random


class Classifier(object):

    def __init__(self, iris):
        #setting the train and test data and targets
        self.iris = iris
        self.d_train, self.d_test, self.t_train, self.t_test = tts(iris.data, iris.target, train_size=.7, random_state=random.randint(400,600))
        self.prediction = []
        self.percent = 0

    def train(self):
        #use this data to come up with an algorithm
        pass

    def predict(self):
        #use this data to set the test results
        for n in range(len(self.t_test)):
            self.prediction.append(0)

    def compare(self):
        #iterate trough the arrays and compare test results
        percent = 0.0
        for n in range(len(self.t_test)):
            if self.t_test[n] == self.prediction[n]:
                percent+=1
        percent = 100*(percent/len(self.t_test))
        self.percent = round(percent,2)
            

    def display(self):
        #print self.t_train
        #print self.prediction
        print 'Accurracy: ' + str(self.percent)+'%'
        
        #print (self.iris.data)
        '''
        # Show the data (the attributes of each instance)
        print (iris.data)
        # Show the target values (in numeric format) of each instance
        print (iris.target)
        # Show the actual target names that correspond to each number
        print (iris.target_names)
        '''

    # these functions are for later
    '''
    def findNN(self, row, k):
        
        distances = []
        category = []
        
        for i in self.d_train:
            distances.append()

    def findInstances(self, rowY, rowX): #iterate through each data type
        i in range
    '''

        
classifier = Classifier(datasets.load_iris())
classifier.predict()
classifier.compare()
classifier.display()



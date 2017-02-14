

class CSV(object):

    def __init__(self, filename = 'diabetes.csv'):
        
        self.file = open(filename, 'r')
        self.data = []
        self.line()
        self.normalize()
        
    def line(self):

        for line in self.file:
            self.parseLine(line)
            
    def parseLine(self, line):

        line = line.replace(',',' ')
        temp = line.replace('  ',' ').replace('\n','')
        temp = (temp.split(' ',len(temp)))
        self.data.append(map(float,temp))

    def normalize(self):
        normArr = []
        maxN = []
        minN = []
        for i in range(len(self.data[0])):
            tmpArr = []
            for d in self.data:
                tmpArr.append(d[i])
            normArr.append(tmpArr)

        for n in normArr:
            maxN.append(max(n))
            minN.append(min(n))

        #print minN, maxN
        normalized = []
        for d in self.data:
            norm = []
            for x,y,z in zip(d, maxN, minN):
                temp = (x-z)/(y-z)
                norm.append(round(temp*100000)/100000)
            normalized.append(norm)

        self.data = normalized

            
            

    def show(self):
        for d in self.data:
            print d


##c = CSV()
##c.normalize()
##c.show()




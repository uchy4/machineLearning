


class CSV(object):

    def __init__(self, filename = 'credit.txt', cut=False):
        
        self.file = open(filename, 'r')
        self.data = []
        self.cut = cut
        self.checkData = []
        self.line()
        self.check()
        
    def line(self):

        for line in self.file:
            self.parseLine(line)
            
    def parseLine(self, line):

        line = line.replace(',',' ')
        temp = line.replace('  ',' ').replace('\n','')
        temp = (temp.split(' ',len(temp)))
        if self.cut:
            self.data.append(temp[1:])
            self.checkData.append(len(temp[1:]))
        else:
            self.data.append(temp)
            self.checkData.append(len(temp))

    def check(self):
        checkedData = []
        temp = sum(self.checkData)/len(self.checkData)
        print temp
        print set(self.checkData)
        for d in self.data:
            if len(d)==temp:
                checkedData.append(d)
        self.data = checkedData
        

    def show(self):
        print self.data



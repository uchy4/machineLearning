class Node:
    def __init__(self,column = -1, level = 0, type='', answer=''):
        self.children = []
        self.level = level
        self.type = type
        self.column = column
        self.answer = answer
        self.parent = 0
        self.isLeaf = True


    def grow(self,temp,parent):
        temp.parent = parent
        self.isLeaf = False
        self.children.append(temp)
        return temp
    def predict(self, test_row):
        for d in test_row:
            self.recur(self.child)

    def recur(self, child):
        if not child.children:
            return child.answer
        else:
            for ch in child.children:
                self.recur(ch)
        
        

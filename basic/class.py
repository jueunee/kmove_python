import 
class fourCal:
    first =0
    second=0
    def _init_(self,first,second):
    def getvalue(self):
        print(self.first)
        print(self.second)

    def setvalue(self,first,second):
        self.first =first
        self.second = second

class1 = fourCal(1,2)
class2 = fourCal(10,20)

class1.setvalue(10,20)
class1.getvalue()
class2.getvalue()
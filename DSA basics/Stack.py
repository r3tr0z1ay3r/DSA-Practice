

class Stack():
    def __init__(self , vals:list) -> None:
        self.stackArr = vals
        self.top = self.stackArr[0]
    
    def stackPush(self,val):
        self.stackArr.insert(0,val)
        self.top = self.stackArr[0]

    def stackPop(self):
        return(self.stackArr.pop(0))
    
    def getStack(self):
        return(self.stackArr)
    
obj = Stack([2,6,1,2,5])
print(obj.getStack())
obj.stackPush(9)
print(obj.getStack())
obj.stackPop()
print(obj.getStack())
obj.stackPop()
obj.stackPop()
obj.stackPop()
print(obj.getStack())
class DeQue():
    def __init__(self,que:list) -> None:
        self.arr = que
        self.size = len(que)
    def pushFront(self,val):
        self.arr.insert(0,val)
        self.size += 1
    def pushBack(self,val):
        self.arr.append(val)
        self.size += 1
    def popFront(self):
        self.arr.pop(0)
        self.size -= 1
    def popBack(self):
        self.arr.pop(-1)
        self.size -= 1
    def getVals(self):
        return self.arr
    def getSize(self):
        return self.size
    
dq_1 = DeQue([4,3])
dq_1.pushBack(10)
dq_1.pushBack(20)
dq_1.popBack()
dq_1.popFront()
dq_1.pushFront(99)
print(dq_1.getSize())
print(dq_1.getVals())
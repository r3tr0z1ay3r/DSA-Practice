import heapq

class Heap:
    def __init__(self,value:list):
        self.heap = value
        heapq.heapify(self.heap) #Heap Left Child -> 2*i + 1 || Right Child -> 2*i + 2
        print(self.heap)
    
    def getMin(self):
        return self.heap[0]
    def extractMin(self):
        return heapq.heappop(self.heap)
    def insertElm(self,val):
        return heapq.heappush(self.heap,val)
    
    
to_heap = [65,21,6,321,12,58,12,65,2,798]

obj = Heap(to_heap)
for i in range(3):
    print(obj.extractMin())
obj.insertElm(69)
print(obj.getMin())

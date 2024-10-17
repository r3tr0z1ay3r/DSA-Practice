class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None
class LRU:
    def __init__(self,capacity) -> None:
        dummy = head = Node()
        for _ in range(capacity-1):
            dummy.next = Node()
            dummy = dummy.next
        dummy.next = head
    def get(self,key):
        pass
    def put(self,key,value):
        pair = {key:value}
        


        
keys = {1:10,2:20}
LRU(2)
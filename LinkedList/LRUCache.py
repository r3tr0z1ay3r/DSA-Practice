"""
Problem:
Implement a Least Recently Used cache with a fixed capacity

Approach:

Initialize a new classe Node to hold the values together
It containts key,val as well as prev and next pointers,
This class implements a double linked list node

Initialize the class with capacity, cache as hashmap and then dummy variable for left and right pointing the least and most recently used
Make these points point to each other to overcome edge cases
In the hashmap we store key -> Pointer having the key val pair


We create two helper functions remove and insert which take the node as attribute
In insert :
    we simple manipulate pointers to remove the node, the current node's prev is updated to the right node's prev and the node's next is update to right node
In remove:
    the node's prevs node's next is update to point to the node's next
    the node's next nodes'prev is updated to point to the node's prev

In get function:
    if the key is in the hashmap, we simple fetch the key and return it
    if not then we return -1

In put function:
    if the key already exists in hashmap:
        we remove the node to the cache
    we update the hashmap with the new value and call the helper function insert to finish the process


"""


class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.prev,self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.cache = {} #Key -> Node
        self.left,self.right = Node(0,0),Node(0,0) #Left is LRU, Right is Most Recently Used 
        self.left.next,self.right.prev = self.right,self.left

    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev
    
    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        prev.next = nxt.prev = node
        node.prev,node.next = prev,nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.limit:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

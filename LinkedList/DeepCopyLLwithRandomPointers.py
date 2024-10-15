"""
Prblm:
Given the head of linked list, This linked list also has a random pointer
This random pointer points to randdom nth index(0-indexed) of the LL

Replicate this list as a deep copy meaning new node should be used to replicate all the pointers

Approach:

Using an hash map , we can assign old Node to the newly created node.
Using this hash map we can iterate through and assign the pointer values .next and .random to the newNode
While looping through we will hit the end that is None or Null, To solve this conflict we add None:None as value into the hashMap 


"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hashed = {None:None}
        while curr:
            newNode = Node(curr.val)
            hashed[curr] = newNode
            curr = curr.next
        curr= head
        while curr:
            print(curr.val)
            copyNode = hashed[curr]
            copyNode.next = hashed[curr.next]
            copyNode.random = hashed[curr.random]
            curr = curr.next
        return hashed[head]
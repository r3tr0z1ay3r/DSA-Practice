# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Prblm:
Given the head of linkedList, with node having (val:holding the data,next:pointer to next node),
Reverse the linked list and return the begining(head) of  the linked list,

Approach,
Iterate through the linkedlist through a while loop,
store the curr's next pointer in a temp var, then swap the next pointer of current elem and the previous elm,
then swap the prev elm with the curr and curr with the temp,
Effectively swapping the elms of prev and curr node

This is repeated through the entire linked list and head is assigned to the last value
"""

class Solution:
    def reverseList(self, head):
        prev,curr =None,head
        while curr:
            temp = curr.next
            curr.next = prev
            prev,curr = curr,temp
        #print(head.val)
        head = prev
        return head
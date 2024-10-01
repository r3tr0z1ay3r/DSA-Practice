# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Prblm:
Given the head of a linked list, you are supposed to remove the nth node from the end of the linked list
Return the the head of the linked list,

Approach:
A linked list can only be traveresed in one direction causing issue when try to remove from the last,
WE can overcome this by having an n gap between a pointer maintaing the length,
So we initiate the left side pointer and then move the right pointer n times to maintain the distance of n betweenm,
after this iterate the LinkedList to get to the end of the LL, At the end the right pointer would be pointing at the end while the left one points at the nth node,
Now we can simple prune the next node and point the left pointer node to the node after the next node.
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0,head)
        prev = temp
        curr = head
        while n > 0:
            curr = curr.next
            n -= 1
        while curr:
            prev = prev.next
            curr = curr.next
        prev.next = prev.next.next
        return temp.next
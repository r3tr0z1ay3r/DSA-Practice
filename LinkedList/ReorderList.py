# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Prblm:
Given the head of singly linked list , reorder that list in [0, n-1, 1, n-2, 2, n-3, ...] order,
n = length of LL without modifying the values of the node

Approach:
Iterate through the list and find the half point using slow and fast pointer approach
By looking at the order, we can see that the order is alternating between first and last val,
Reverse the second half of LL so that order is from last to first, allowing us to merge and form the required order
Alternate through the two pointers at both start and end and combine them to form the required order,
For iteration to merge, we can use the second half as limit as the second half will always be equal or lesser than the first half regardless of if the length is even or odd

Note:
We can also add the nodes themself to an array and use two pointer approach to modify thier next value 
However, This would have the memory complexity of O(n) whereas current approach would have O(1) complexity
"""
class Solution:
    def reorderList(self, head) -> None:
        slowp,fastp = head,head.next
        while fastp and fastp.next: #Navigating to the middle point of the LL to split halves
            slowp = slowp.next
            fastp = fastp.next.next
        
        first,second = head,slowp.next
        prev = slowp.next = None #Assign None to both prev and slowp.next var 

        while second: #Reversing the second half of the LL.
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        second = prev
        while second: #Merging the both halves to form the order
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2
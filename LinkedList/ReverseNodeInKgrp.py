"""
Intituion:
    Add nodes to a list , when list reaches k , add the ll in the list
    return LL, repeat until we run out of nodes and the remains if any

Approach:
    maintain a list for nodes to reverse and append nodes to it
    each of the node points to the next node in the list
    when list reaches k, return the first node(points to the rest of the nodes) to the dummy head,empty the list

    Continue this loop until we reach the end of the node,
    if any nodes remains in the list, attach them to returnable LL
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseKGroup(self,head,k):
        curr = head
        ret_LL = dummy = ListNode()
        while curr:
            to_reverse = []
            for i in range(0,k):
                temp = curr.next
                prev = curr
                curr.next,prev.next = prev,temp
                to_reverse.append(prev)
            print(to_reverse)
                

obj = Solution()
head1 = [1,2,3,4,5,6]
k =3
obj.reverseKGroup(head1,k)

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
    Given Solution:
        Intituion:
            We get the kth element to form the group, reverse the nodes before it,
            Then attach the kth element back to the linked List.loop this until we can form any group
        Approach:
            We create a loop until with the condition to form group as long as possible
            Create a sub function that fetches the kth element that forms the group,and return that node

            From this kth element we get the next element to the kth group and the group prev is initially set to the dummy node val
            This value will later be updated to the come right to the kth elemet prev val

            We create a loop to reverse the elemets with two pointer approach, prev and curr are set to the next on elem and groupPrev elm
            we then update group prev value to the next elem after the group prev

            This main loop is repeated until we can form the group in the list
        and return the dummy heads

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

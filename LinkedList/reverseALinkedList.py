# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Prblm:
Given the head of linkedList, with node having (val:holding the data,next:pointer to next node),
Reverse the linked list and return the begining(head) of  the linked list,

Approach(Not Solved),
Iterate through the linkedlist through a while loop,
store the curr's next pointer in a temp var, then swap the next pointer of current elem and the previous elm,
then swap the prev elm with the curr and curr with the temp,
Effectively swapping the elms of prev and curr node

This is repeated through the entire linked list and head is assigned to the last value

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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self,head,k):
        dummy = ListNode(0,next=head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev,k) #Returns the kth group node
            if not kth:
                break
            groupNext = kth.next
            prev,curr = kth.next,groupPrev.next #Since we are reversing we point the prev to next group starting
            while curr != groupNext: #Loop for reversing the nodes
                temp = curr.next
                curr.next = prev
                prev,curr = curr,temp
            temp = groupPrev.next #Updating the groupPrev element
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
    def getKth(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
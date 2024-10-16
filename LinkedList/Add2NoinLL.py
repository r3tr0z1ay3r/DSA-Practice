"""
Prblm:
Given two linked list representing numbers in reverse order (ones->tens->hunderds)
Add the values in the both linked list and return the head of the resulting linked list
Each node can only have one digit in them, in case of a double digit sum it should be carried forward to the next number(Linke in normal addition)

Approach:
We create the head of the resulting linkedList and intitate a carry variable to 0 to contain the carry value
Iterate through both the linked list until either there is l1 or l2 or the carry
we add the value of the curr node of each linked list 
We find the carry value(Ones place) by dividing this value by 10 and getting its quotient
We find the value to add to the node(Tens place) by dividing by 10 

We form the node with new value and then add it to the existing linked list

Update all the pointers to its next value 
"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr_res = head
        curr_l1,curr_l2 = l1,l2
        carry = 0
        while curr_l1 or curr_l2 or carry:
            val1 = curr_l1.val if curr_l1 else 0
            val2 = curr_l2.val if curr_l2 else 0

            added = val1 + val2 + carry
            carry = added // 10 # getting the Ten's place
            added = added % 10 # Only getting the one's place
            curr_res.next = ListNode(added)

            curr_res = curr_res.next
            curr_l1 = curr_l1.next if curr_l1 else None
            curr_l2 = curr_l2.next if curr_l2 else None

        curr = head
        while curr:
            print(curr.val)
            curr = curr.next
        return head.next
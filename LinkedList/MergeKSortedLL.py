"""
Intiution:
    Grab all the heads of each LL under the list
    Compare each elm and add the smalest into a new LL 
    Repeat till we reach the end or run out of elems in every head

Approach:
    Divide the problem into a sub problem of merging two sorted list,
    Loop through the list of LL in steps of 2,gathering two LL at once,
    Use an helper function to compare and add the least of two LL node to the tail
    We store all the lists merges into a single arr,
    at the end of merges we combine the merge into a single list

    By repeating this we pair up two lls together and those two together,
    This goes on until there is only a single merged linked list at which point we will stop the loop
    and return the head of that merged list


"""





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not lists:
            return None
        while len(lists) > 1:
            merged_list = []
            for i in range(0,len(lists),2): #Since we are taking two LL at once , increament by 2
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged_list.append(self.mergeList(l1,l2))
            lists = merged_list
        return lists[0]

    def mergeList(self,l1,l2): #Helper function to compare and combine two linked lists
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next












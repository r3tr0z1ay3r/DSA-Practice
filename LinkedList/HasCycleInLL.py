"""
Prblm:
Given a head of linked list, find if there is a cycle in the linked list(a next value of tail loops to an already existing value)
return true if there is a cycle else return false, 
Also given internally a index value is maintained to show which index it it loops to the elem, if there is no loop then it is -1,
however this value is accessible

Approach:
We iterate through the linked list and maintain a hash table with a value and its index,
we do a check to if we already have that value in the hash table, if we have that we return True indicating a cycle,
after we have iterated through the entire LL and we sitll havent returned anything means that we did not find a cycle,
at this point we can return False to indicate that there is no loops in the linkedlist.

"""



class Solution:
    def hasCycle(self, head) -> bool:
        visited = {}
        curr,ind = head,0
        while curr:
            if curr.val in visited.keys():
                print(curr.val,"is looping")
                return True
            visited[curr.val] = ind
            curr,ind = curr.next,ind+1
        print(visited)
        return False
"""
Problem:
    Given prisoners count n, sweets available m and ,start from s
    Prisoners are sat in a circular table hence it comes full circle everytime
    From the sth chair distribute m sweets, return the last prisoner who gets the sweet

My approach:
    Create a circular linked list of all the available prisoners,
    use a flag to start the count from the starting prisoner and move throught the LL to reach the last prisoner
    Return the last node's value

    Flaws:
        Required much more memory than available causing runtime errors
Approach:
    We use division to keep a track of loop
    From the starting point we move the till the amount of sweets,
    Everytime we complete a loop we evenly divide amongst the prisoners and have no remainders
    Hence when we get the remainder we know how much of the loop we have left
    By getting this remainder we can know the prisoner who gets the last of the sweet

    We offset the values by 1 to get a 0th index iteration


    
"""

class LLNode():
    def __init__(self,val=None):
        self.value = val
        self.next = None

def saveThePrisoner(n, m, s):
#   Creating a linked list to represent the prisoners in circle
    dummy = curr = LLNode()
    for i in range(1,n+1):
        newNode = LLNode(i)
        curr.next = newNode
        curr = curr.next
    curr.next = dummy.next
    LL_curr = curr
    count = 1
    start_count = False
    while True:
        if count == m:
            break
        if LL_curr.value == s:
            start_count = True
        if start_count:
            count += 1
        LL_curr = LL_curr.next
    print(LL_curr.value)
    return LL_curr.value

def SaveThePrisoner(n,m,s):
    print(((s-1+m-1)%n)+1)
        
print(SaveThePrisoner(5,5,1))
print(1%5)
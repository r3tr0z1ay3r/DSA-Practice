"""
prblm:
    Give three numbers i,j,k
        i -> starting day
        j -> end day
        k -> divsor no
    in the range of i to k, find the different btwn the number 
    and check whether if the difference is divisible by k

    return the number of days that satisfy the above condition

intituion:
    Find the difference between no and its reversed and check if the remainder of the divison is 0
    keep count of it and return this count

approach:
    we maintain a empty list to get the acceptable days
    we create a for loop within the range specified by i,j
    we can reverse the number by doing a string reversal and find its difference with the unreversed no
    check if the modulo of the division is 0, if so add to the list
    continue this until we exhaust the list

    at the end return the length of the list which contains all the acceptable days
"""

def beautifulDays(i, j, k):
    accepted = []
    for day in range(i,j+1):
        num1 = day
        reversed_num1 = int(str(day)[::-1])
        diff = num1-reversed_num1
        if diff%k == 0:
            accepted.append(day)
    return len(accepted)
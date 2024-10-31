"""
Problem:
    Given two integer list, keyboards and drives each having prices of them respectively and an integer budget
    Find the maximum of the budget we can use to buy one keyboard and drives and return it
    If there are no way of buying from given lists, return -1

Intituion:
    Brute Force:
        Loop through each value of the both list and added the value,
        If the value comes within the budget and greater than our current budget update the current budget

Approach:
    Nested loops to iterate through each items in both the list,
    Intialize the current budget to a value of -1 to handle edge cases
    Find the sum of each pair and if this sum is greater than current budget and lower than given budget
    Update the current budget to this sum,
    
    At the end of the loop return the current budget

"""

def getMoneySpent(keyboards, drives, b):
    max_budget = -1
    for kb in keyboards:
        for drv in drives:
            added = kb+drv
            if added > b:
                continue
            max_budget = max(max_budget,added)
    return max_budget
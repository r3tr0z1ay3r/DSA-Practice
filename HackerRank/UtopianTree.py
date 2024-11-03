"""
Problem:
    Given no of growth cycle, each growth cycle contains spring and summer
    During spring the height increase double the previous heigjt
    During Summer the heigh increases by 1 to the previous height

    return the height at the end of the growth cycle
Intiution:
    By Identifying if the nth cycle is even or not we can identify if its summer or spring
    And accordingly increase the height
Approach:
    we start a loop for the growth cycle n
    initially we set the height to 1 i.e during first cycle
    After which we check if the nth cycle is even or odd,
    If even it means that it summer as we start at spring, since summer we add the height by 1
    If odd it means the its spring,since spring we double the height

    We continue this process till the end of the loop(we got n+1 in the loop as by deaul it loops to n-1)
    return the height
"""

def utopianTree(n):
    for i in range(0,n+1):
        if i == 0:
            height = 1
        elif i%2 == 0:
            height += 1
        else:
            height *= 2
    return height
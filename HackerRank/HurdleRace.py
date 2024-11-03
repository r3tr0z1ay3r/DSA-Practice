"""
Problem:
    given a list of heights of hurdle and the limit to jump k
    k can be increased by taking magic potion which increases k by 1
    How many potions should be taken to finish the race

Intiution:
    The difference between the maximum height of the hurdle and jump limit
    gives the potion intake

Approach:   
    Using max fn we can find the max of the height and then to which we can subtract jump limit k 
    to find the poition usage

    To handle edge cases we check if this difference is bigger than 0 before updating the count
"""


def hurdleRace(k, height):
    count = 0
    if max(height)-k > 0:
        count = max(height)-k
    return count
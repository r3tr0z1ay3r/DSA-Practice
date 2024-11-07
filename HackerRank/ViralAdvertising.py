"""
Prblm:
    A ad is aired, initially it is shared to 5 people,
    Half of the people who recieve the ad like it,
    The people who likes the ad shares it to exactly three people,
    At the given nth day, find the cumulative likes and return it

Intiution:
    Simple Mathematical calulcation within a loop can be used
    Updating values at it changes

Approach:
    We initialize variable to keep track of the people shared and total likes
    We intialize loop for each day, at each iteration, we update shared to reflect the amount of people as required

    Shared is divided by 2 as half the people like it and is given to another variable
    the shared variable is updated by multiplying the liked by 3
    the total like variable will be update at each iteration to reflect the changes done to it


    This loop executes until the nth day and returns the total like
"""

def viralAdvertising(n):
    shared = 5
    total_likes = 0
    for days in range(1,n+1):
        liked  =  shared // 2
        total_likes += liked
        shared = liked * 3
    return total_likes
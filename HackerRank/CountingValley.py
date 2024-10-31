"""
Problem:
    Given an string representing the path taken by a hiker,
    It contains D for Downstep and U for upstep,
    A valley is indicated by going D and then return to surface level by U
    Find the the number of valleys that the hikers have taken

Intituion:
    Maintain a numerical way of identifying valley entrance and exit
    Count the exits from valley to get the number of valleys 
Approach:
    Use an hashmap to map U to +1 and D to -1
    Maintain the step taken by the hiker reducing and increasing,
    When the number falls below zero we know the hiker is in an valley,use an flag to indicate currently in valley
    When the number of step reaches zero and the flag is true, The hiker have cluimber out of the valley,increase the count of valley


"""
def countingValleys(steps, path):
    paths = {'U':1,'D':-1}
    steps_taken,valley_count = 0,0
    in_valley = False
    for i in path:
        steps_taken += paths[i]
        if steps_taken < 0:
            in_valley = True
        if in_valley and steps_taken == 0:
            print("In valley reset")
            valley_count += 1
            in_valley = False
        print(steps_taken)
    return valley_count
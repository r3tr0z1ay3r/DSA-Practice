"""

piles are bananas which are to be eaten, every ith elm has i bananas
have to determine a k such that the entire pile can be eaten in h hours
k - > rate of bananas eaten per hr, cannot move to next pile without depleting current pile
cannot move to next pile in the same hr even when done 

sol
find a mid by using largest and smallest elm, compare if mid depletes the pile within h,
calculate time required for current mid which is k,
if this time is less than h, change result to k,and the right pointer is updated to the previous elm of current right
if not left pointer is incremented, repeated till all values are found
if 
"""
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l_rate,h_rate = 1,max(piles)
        res = max(piles)
        while l_rate <= h_rate:
            estK = l_rate + h_rate // 2
            timeTaken = 0
            for banana in piles:
                timeTaken += ceil(banana/estK)
            print(timeTaken)
            if timeTaken < h:
                res = estK
                print("Updating res to {}".format(res))
                h_rate = estK-1
            else:
                l_rate = estK + 1
        return res

obj = Solution()
pile1,h1 = [1,4,3,2], 9
piles2=[25,10,23,4]
h2=4
print(obj.minEatingSpeed(pile1, h1))
        
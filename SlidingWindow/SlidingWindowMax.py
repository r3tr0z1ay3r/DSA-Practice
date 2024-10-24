"""
Intitution:
    Create a left pointer at left edge and move it k times to right
    Append the max of that window to list and move the window

Approach:
    Create a l and right pointer with left point at left edge and right pointing at the window size (k)
    loop thro the logic until the right pointer reaches the end
    for each step, create a subset of l -> r
    Get the max value from this window and append it to the return array

    After the end, return the return arr
"""

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l,r = 0,k
        ret = []
        while r <= len(nums):
            window = nums[l:r]
            ret.append(max(window))
            l += 1
            r += 1
        print(ret)
        return ret
obj = Solution()
nums1 = [1,2,1,0,4,2,6]
k1 = 3
obj.maxSlidingWindow(nums1,k1)
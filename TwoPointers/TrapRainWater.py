"""
Problem:
Given an non zero int array of heights, find the water that can be trapped within those heights
Return the max area that can be trapped within the bars

Approach (2 pointer):
Take two pointer on left and right,
compare which of the two pointer is lesser and move it to the next val,
at the current val, get the minimum value of that pointer and subtract that with the current height,
if that value is non negative , add that value to the result value and update the min of the pointer to the lesser value,
move the pointer to the next element and repeat the process.

"""


class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        l,r = 0,len(height)-1
        leftMax,rightMax = height[l],height[r]
        result = 0
        while l < r:
            if leftMax<rightMax:
                l += 1
                leftMax = max(leftMax,height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax,height[r])
                result += rightMax - height[r]
        return result


obj = Solution()
height = [0,2,0,3,1,0,1,3,2,1]
print(obj.trap(height))
        
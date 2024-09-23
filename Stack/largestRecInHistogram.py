"""
prblm:
given an array heights, it contains ints of represeting heights of bar in histogram,
width of these bars are 1,
find the area of the largest rectangle which can formed within the histogram (l*b)

approach:
to form a rectange in the histogram the current value should be followed by a larger value,
by monitoring this change we can identify to which end we can extend the rectangle,
we maintain a stack holding the values of index and height of each bar, when we see that value in the stack is larger than the current val being considered,
we will pop that value and compute the total area that can formed within the index and height, we will then update the index of the value to which we can extend to the stack while appending it,
we repeat this and iteratively update the max area where needed,

after all the looping if there are still values in the stack that means that we have rectangles lasting till the end of histogram,
we simply compute the area for all these values and update if neseccary

"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] #Having ind:val pair

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind,height = stack.pop()
                maxArea = max(maxArea,(height*(i-ind)))
                start = ind
            stack.append((start,h))
        for i,h in stack:
            maxArea = max(maxArea,h*(len(heights)-i))
        print(maxArea)

obj = Solution()
heights = [1,3,7]
obj.largestRectangleArea(heights)
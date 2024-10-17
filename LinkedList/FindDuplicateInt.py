"""
Prblm:
Given an array of integers containing n+1 intergers,
Each integer in nums is in the range (1,n). 

Each of this integer exactly once , only one integer which appears two or more times
Return the integer that repeats

Approach-1:
Iterate through the each element and append that to the list,
Check if the list contains the element in the list, if so return that integer

Approach - 2:
Iterate through the loop, At each iteration 
Check the count of number of current element, if it exceeds 1 , return that int
Repeat until we reach that conclusion

Solution Given:


"""
class Approach1:
    def findDuplicate(self, nums: list[int]) -> int:
        hashed = []
        for i in nums:
            if i in hashed:
                return i
            else:
                hashed.append(i)

class Approach2:
    def findDuplicate(self, nums: list[int]) -> int:
        for i in nums:
            if nums.count(i) > 1:
                return i
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
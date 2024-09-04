class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r = 0 , len(numbers)-1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l+1,r+1]
            
"""
Note to self:
Since the values are sorted we can use an approach similar to binary serach
hence the two pointer approach

"""
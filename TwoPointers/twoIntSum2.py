class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r = 0,len(numbers)-1
        sums = 0
        while l<r:
            sums = numbers[l] + numbers[r] #caluclate current sum
            if sums == target: 
                return [l+1,r+1]
            if sums > target: #Move right pointer if sum lower than target since arr sorted
                r -= 1
            if sums < target:
                l += 1
        return False #If there is no valid solution
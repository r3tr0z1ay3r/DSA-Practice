from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash_map = defaultdict(list)
        for i in set(nums):
            curr = i
            while (curr+1) in nums:
                hash_map[i].append(curr+1)
                curr = curr+1
            hash_map[i] = len(hash_map[i])+1
        print(max(hash_map.values()))







nums = [0,3,2,5,4,6,1,1]
obj1 = Solution()
obj1.longestConsecutive(nums)




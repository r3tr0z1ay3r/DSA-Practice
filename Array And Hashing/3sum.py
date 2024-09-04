from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        first_pointer = nums[0]
        second_pointer = len(nums)-1
        to_sum,return_arr = [],[]
        
        for i in range(len(nums)):
            if len(to_sum) == 2:
                val = first_pointer + sum(to_sum)
                if val == 0:
                    return_arr.append([first_pointer,to_sum[0],to_sum[1]])
                to_sum.pop(0)
            to_sum.append(nums[second_pointer])
            second_pointer -= 1
        hash_arr = defaultdict(list)
        print(return_arr)
        for i in return_arr:
            hash_arr[return_arr.count(i)] = i
        return_arr = []
        for i in hash_arr.keys():
            print(hash_arr[i])
            return_arr.append([val[i] for val in hash_arr])
        print(return_arr)
        return return_arr
        


obj1 = Solution()
nums1 =[0,0,0,0]
nums = [-1,0,1,2,-1,-4]
obj1.threeSum(nums)
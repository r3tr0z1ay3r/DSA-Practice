from collections import defaultdict

class SolutionOWN:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        first_pointer = nums[0]
        second_pointer = len(nums)-1
        to_sum,return_arr = [],[]
        used_vals = {}
        for i in nums:
            used_vals[i] = False
        for i in range(len(nums)):
            if len(to_sum) == 2:
                val = first_pointer + sum(to_sum)
                print(used_vals)
                if val == 0 and not (used_vals[to_sum[0]] and used_vals[to_sum[1]]):
                    return_arr.append([first_pointer,to_sum[0],to_sum[1]])
                    used_vals[to_sum[0]],used_vals[to_sum[1]] = True,True
                to_sum.pop(0)
            to_sum.append(nums[second_pointer])
            second_pointer -= 1
        print(return_arr)

class SolutionSOL():
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res_arr = []
        nums.sort()

        for i,a in enumerate(nums):
            if a>0:
                break
            if i>0 and a== nums[i-1]:
                continue
            left,right = i+1,len(nums)-1
            while left<right:
                threeSum = a+nums[left]+nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res_arr.append([a,nums[left],nums[right]])
                    l += 1
                    r -= 1
                    while nums[left] == nums[l-1]:
                        l+= 1
        return res_arr

obj1 = SolutionSOL()
nums1 =[0,0,0,0]
nums2=[-1,0,1,0]
nums = [-1,0,1,2,-1,-4]
obj1.threeSum(nums2)
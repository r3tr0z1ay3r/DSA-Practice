def getProd(arr:list):
    prod = 1
    for i in arr:
        prod *= i
    return prod


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        return_arr = []
        hash_prod = {}
        print(len(nums))
        for i in range(0,len(nums)):
            dupe = nums.copy()
            dupe.pop(i)
            print(i,dupe)
            hash_prod[i] = getProd(dupe)
        return_arr = [i for i in hash_prod.values()]
        print(return_arr)



nums = [1,2,4,6]
obj = Solution()
obj.productExceptSelf(nums)
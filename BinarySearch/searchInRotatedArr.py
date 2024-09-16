class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        while l <= r:
            mid = l + (r-l) // 2
            print(l,r ,"added is the mid val {}".format(mid))
            if nums[mid] == target:
                return mid
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] > nums[r]:
                l = mid + 1
                print("updatin l to {}".format(l))
            else:
                r = mid - 1
        return -1
obj = Solution()
nums1 = [1,3]
target1 = 3
print(obj.search(nums1,target1))
        
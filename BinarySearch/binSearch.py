class Solution:
    def search(self, nums: list[int], target: int) -> int:
        mid = len(nums) // 2
        l,r = 0,len(nums)-1
        while l<=r:
            print(l,r,mid)
            mid = (l + (r-l)// 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            if nums[mid] > target:
                r = mid-1
        return -1 #When not in arr
obj = Solution()
nums1,target1 = [-1,0,2,4,6,8],4
nums2 = [-1,0,2,4,6,8]
target2 = 3


print(obj.search(nums2,target2))
        
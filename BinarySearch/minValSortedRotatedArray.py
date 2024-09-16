"""
prblm:

Ascending order initially but when given as input rotated n times,
where n is the length of array, while rotating the n values in the last are moved to the front and swapped,
Find a O(log n) ,values are unique meaning no dupes, rotatin array n time gives original arr

approach:

since value in the middle can be classified into mid point having lower and higher values to either side
binary search can be used to find the min val in log n time
vals are higher and lower to either side as rotating only moves value to the left or right

"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r = 0,len(nums)-1
        curMin = float("inf")
        while l <= r:
            mid = l + (r-l)//2
            curMin = min(curMin,nums[mid])
            print(mid, nums[mid],nums[mid+1])
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid-1
        return curMin
    
nums1 = [3,4,5,6,1,2]
obj = Solution()
print(obj.findMin(nums1))
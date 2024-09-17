"""
Prblm:
two array given which are sorted with m and n size
return the median value, find the median among the two

Proposed Approach:
Two pointers, compare each and combine into a single array
Find the median by gathering middle most elm

Actual Approach:
in the lower sized arr, we run binary search to find the mid val,
by comparing this middle value with the middle+1 val of the other arr we can find out if the parition is valid or not,
if the lower sized arr(A) left is greater than the other arr(B) and vice versa is true , then parition is valid:
if either of this is not true then parition is not valid:
In which case we move the pointers in the array to fix it,
if the Aleft is greater than the Bright then move the left pointer to mid-1
if the Bleft is greater than Aright then move the right pointer to mid + 1

This binary search repeated until we get a valid parition, from here finding the median is divided into 2 cases:
If even case:
    we take the max of left parition and min of right parition and divide by 2 to get median,
if odd case:
    we simply return the min of right parition

Note: To tackle the edge case of either right of left parition being empty, we set the default value to +infinity and -infinity to right andleft parition if there are no values
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a,b = nums1,nums2
        if len(b) < len(a):
            a,b = b,a
        total = len(nums1)+len(nums2)
        half = total // 2
        l,r = 0,len(a)-1 #running binary search on the least value arr
        while True: #Since guarenteed to have a median val
            i = l+r // 2
            j = half-i-2 #Instead of finding mid for B , by subtracting current A half from B we can find B mid but since we used Len fn we need balance out by doing -2 for +1 +1 obtained from two len fns
            
            A_left = a[i] if i >= 0 else float("-inf") #Finding mid val, if none then its -infinity
            A_Right = a[i+1] if (i+1) < len(a) else float("inf") #Finding the adjacent value to compare for parition , if none +inf
            B_left = b[j] if j >= 0 else float("-inf")
            B_Right = b[j+1] if (j+1) < len(b) else float("inf")

            if A_left <= B_Right and B_left <= A_Right:
                if total % 2:
                    return min(A_Right,B_Right) #Getting the min from right parition
                else:
                    return (max(A_left,B_left)+min(A_Right+B_Right)) / 2
            elif A_left > B_Right:
                r = i - 1
            else:
                l = i + 1

        
obj = Solution()
nums1 = [1,3]
nums2=[2]
obj.findMedianSortedArrays(nums1,nums2)
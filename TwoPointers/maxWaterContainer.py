class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left,right,max_area = 0,len(heights)-1,0 #Initialising variables and pointers
        while left < right: #Ensuring a condition where pointers dont go across each other
            print(heights[left],heights[right],heights[right]*(right-left))
            max_area = max(max_area,min(heights[left],heights[right]) * (right-left)) #Updating the area by calculating area
            if heights[left] < heights[right]: #Compare the heights of each wall and move as neseccary
                print("Moving left")
                left += 1
            elif heights[right] <= heights[left]:
                print("Moving right")
                right -= 1
            print("Max area is {}".format(max_area))
        return max_area


"""

Input: height = [1,7,2,5,4,7,3,6]

Output: 36

Visualise each value in height as a bar chat and as wall of container
By using the two pointer approach we can move the pointer across and find the largest possible container
area is found by the height*length , length being the distance between the height values found using the index
always use the minimum of the either wall to ensure proper amount of water stored

"""
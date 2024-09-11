class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top,bot = 0,len(matrix)-1
        #mid_row = top + (bot-top) // 2
        while top <= bot:
            mid_row = top + (bot-top) // 2
            if target in matrix[mid_row]:
                break
            if matrix[mid_row][-1] > target:
                bot = mid_row - 1
                print("UPdating bot to {}".format(bot))
                continue
            if matrix[mid_row][-1] < target:
                top = mid_row + 1
                print("Updatin Top to {}".format(top))
                continue

        l,r = 0 , len(matrix[0])-1
        while l <= r:
            mid = l + (r-l) // 2
            if matrix[mid_row][mid] < target:
                l = mid + 1
            elif matrix[mid_row][mid] > target:
                r = mid - 1
            else:
                return True
        return False

obj = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
target = 10
print(obj.searchMatrix(matrix1,target1))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot = 0,len(matrix)-1
        while top <= bot:
            mid_row = top + (bot-top) // 2
            if matrix[mid_row][-1] > target:
                bot -= 1
            if matrix[mid_row][-1] < target:
                top += 1
            else:
                break
        if not (top <= bot):        
            return False
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

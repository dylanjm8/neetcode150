class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        top, bot = 0, (rows - 1)

        while top <= bot:
            row = top + bot // 2 
            if (matrix[row][0] > target):
                bot = (row - 1)
            elif (matrix[row][-1] < target):
                top = (row + 1)
            else:
                break

        if not (top <= bot):
            return False

        row = top + bot // 2 # found row

        # now we search horizontally
        
        l , r  = 0, cols-1

        while l <= r:
            mid = r + l // 2

            if (matrix[row][mid] < target):
                l = mid + 1
            elif (matrix[row][mid] > target):
                r = mid - 1
            else:
                return True

        return False
            
                


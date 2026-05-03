class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l,r = 0, ROWS - 1
        m = 0
        while l <= r:
            m = (l + r) // 2
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                break
        row = m
        left, right = 0, COLS-1
        while left <= right:
            m = (left + right) // 2
            if target > matrix[row][m]:
                left = m + 1
            elif target < matrix[row][m]:
                right = m - 1
            else:
                return True
        return False
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS,COLS = len(matrix), len(matrix[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    q.append((r,c))
        while q:
            row,col = q.popleft()
            for i in range(ROWS):
                matrix[i][col] = 0
            for i in range(COLS):
                matrix[row][i] = 0
        
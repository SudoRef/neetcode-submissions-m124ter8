class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        
        q = deque()
        ROWS,COLS = len(matrix),len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    q.append((r,c))
        def check(row,col):
            return 0 <= row < ROWS and 0 <= col < COLS
        while q:
            row,col = q.popleft()
            dirs = [[0,1],[1,0],[0,-1],[-1,0]]

            for d_row, d_col in dirs:
                new_row = row + d_row
                new_col = col + d_col
                while check(new_row, new_col):
                    matrix[new_row][new_col] = 0
                    new_row+=d_row
                    new_col+=d_col


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS,COLS = len(matrix),len(matrix[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    q.append((r,c))
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        def check(row,col):
            return 0 <= row < ROWS and 0 <= col < COLS
        while q:
            row,col = q.popleft()
            for d_row,d_col in dirs:
                new_r = row + d_row
                new_c = col + d_col
                while check(new_r,new_c):
                    matrix[new_r][new_c] = 0
                    new_r+=d_row
                    new_c+=d_col


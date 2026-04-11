class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS,COLS = len(matrix),len(matrix[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    q.append((r,c))
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        def check(row,col):
            return 0 <= row < ROWS and 0 <= col < COLS
        while q:
            row,col = q.popleft()
            for d_r,d_c in dirs:
                n_r = row + d_r
                n_c = col + d_c
                while check(n_r,n_c):
                    matrix[n_r][n_c] = 0
                    n_r+=d_r
                    n_c+=d_c

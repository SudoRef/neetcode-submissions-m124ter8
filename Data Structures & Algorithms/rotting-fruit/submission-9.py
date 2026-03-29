class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()

        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((0,r,c))
        res = 0
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        def check(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1
        while q:
            minutes,r,c = q.popleft()
            res = minutes

            for d_r,d_c in dirs:
                new_r,new_c = r + d_r, c + d_c
                if check(new_r,new_c):
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    q.append((minutes+1,new_r,new_c))
        return res if fresh == 0 else -1

            
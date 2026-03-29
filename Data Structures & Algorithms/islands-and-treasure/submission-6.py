class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid),len(grid[0])
        visited = set()

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((0,r,c))
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        def check(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] > 0
        while q:
            curr,r,c = q.popleft()
            for dir_r, dir_c in dirs:
                new_r, new_c = dir_r + r, dir_c + c
                if check(new_r, new_c) and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    grid[new_r][new_c] = curr+1
                    q.append((curr+1, new_r, new_c))
        
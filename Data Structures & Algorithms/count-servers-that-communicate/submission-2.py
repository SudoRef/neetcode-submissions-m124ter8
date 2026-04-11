class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid),len(grid[0])
        res = 0

        def check(row):
            res = 0
            for col in range(len(grid[0])):
                if grid[row][col]:
                    curr_r, curr_c = row,col
                    for i in range(ROWS):
                        if grid[i][col] == 1 and i != curr_r:
                            return True


        for r in range(len(grid)):
            curr = sum(grid[r])
            if curr > 1:
                res+=curr
            elif curr == 1 and check(r):
                res+=1
        return res
                
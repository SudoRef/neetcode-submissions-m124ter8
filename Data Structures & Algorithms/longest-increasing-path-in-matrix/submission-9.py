class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS =len(matrix),len(matrix[0])
        dp = {}

        def check(r,c,prev):
            return 0 <= r < ROWS and 0 <= c < COLS and matrix[r][c] > prev

        def dfs(r,c,prev):
            if not check(r,c,prev):
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            prev = matrix[r][c]
            res = 0
            res = max(res, dfs(r+1,c,prev)+1)
            res = max(res, dfs(r-1,c,prev)+1)
            res = max(res, dfs(r,c+1,prev)+1)
            res = max(res, dfs(r,c-1,prev)+1)
            dp[(r,c)] = res
            return res
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)
        return max(dp.values())
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j == len(p):
                return i == len(s)
        
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            dp[(i,j)] = False
            if j + 1 < len(p) and p[j+1] == "*":
                res = dfs(i,j+2) or (match and dfs(i+1,j))
                dp[(i,j)] = res
            elif match:
                res = dfs(i+1,j+1)
                dp[(i,j)] = res
            return dp[(i,j)]
        return dfs(0,0)

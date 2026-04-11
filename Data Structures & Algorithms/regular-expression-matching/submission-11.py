class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == len(s) and j == len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            res = False
            if j + 1 < len(p) and p[j+1] == '*':
                res = dfs(i,j+2) or (match and dfs(i+1,j))
                return res
            if match:
                res= dfs(i+1,j+1)
                return res
            
            dp[(i,j)] = res
            return dp[(i,j)]
        return dfs(0,0)
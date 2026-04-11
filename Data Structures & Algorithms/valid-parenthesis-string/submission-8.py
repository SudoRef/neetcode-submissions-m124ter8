class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}

        def dfs(open,i):
            if i == len(s):
                return open == 0
            if open < 0:
                return False
            if (open,i) in dp:
                return dp[(open,i)]
            res = False
            if s[i] == '(':
                res = dfs(open+1,i+1)
            elif s[i] == ')':
                res = dfs(open-1,i+1)
            else:
                res = dfs(open+1,i+1) or \
                        dfs(open-1,i+1) or \
                        dfs(open,i+1)
            dp[(open,i)] = res
            return res
        return dfs(0,0)
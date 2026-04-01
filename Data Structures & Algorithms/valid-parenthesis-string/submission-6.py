class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        
        def dfs(open,i):
            if i >= len(s):
                return open == 0
            if open < 0:
                return False
            if (open,i) in dp:
                return dp[(open,i)]
            if s[i] == '(':
                dp[(open,i)] = dfs(open+1,i+1)
            elif s[i] == ')':
                dp[(open,i)] = dfs(open-1,i+1)
            else:
                dp[(open,i)] = max(dfs(open+1,i+1),dfs(open-1,i+1),dfs(open,i+1))
            return dp[(open,i)]
        return dfs(0,0)

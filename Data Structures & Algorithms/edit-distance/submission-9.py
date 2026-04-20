class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = {}

        def dfs(i,j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i,j) in dp:
                return dp[(i,j)]
            res = 0
            if word1[i] == word2[j]:
                return dfs(i+1,j+1)
            else:
                res = min(dfs(i,j+1),dfs(i+1,j),dfs(i+1,j+1))+1
                dp[(i,j)] = res
            return dp[(i,j)]
        return dfs(0,0)
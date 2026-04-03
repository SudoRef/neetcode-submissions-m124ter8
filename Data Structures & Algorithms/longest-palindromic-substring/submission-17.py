class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        start = 0
        l = 1
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] == s[j]:
                    if j - i < 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j - i + 1 > l:
                            l = j - i + 1
                            start = i
        return s[start: start+l]
class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

    def addWord(self, s: str):
        cur = self  
        for c in s:
            if c not in cur.children:      
                cur.children[c] = TrieNode()
            cur = cur.children[c]     
        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self
        res = 0
        for i in range(len(word)):
            c = word[i]
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.eow

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(len(s)-1,-1,-1):
            dp[i] = dp[i + 1] + 1

            for j in range(i, len(s)):
                if s[i:j+1] in word_set:
                    dp[i] = min(dp[i], dp[j + 1])
        return dp[0]

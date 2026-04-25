class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx = {}
        for i in range(len(s)):
            idx[s[i]] = i
        curr = 0
        l = 0
        res = []
        for i in range(len(s)):
            ch = s[i]
            curr = max(curr, idx[ch])
            if curr == i:
                res.append(i-l+1)
                l = i+1
        return res

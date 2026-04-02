class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i, ch in enumerate(s):
            lastIdx[ch] = i
        end = 0
        res = []
        curr = 0

        for i, ch in enumerate(s):
            end = max(end, lastIdx[ch])
            curr+=1
            if i == end:
                res.append(curr)
                curr = 0
        return res
            


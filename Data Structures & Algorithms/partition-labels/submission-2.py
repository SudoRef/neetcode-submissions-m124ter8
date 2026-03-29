class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}

        for i, ch in enumerate(s):
            lastIdx[ch] = i
        end = 0
        size = 0
        res = []
        for i, ch in enumerate(s):
            size+=1
            end = max(end, lastIdx[ch])
            if i == end:
                res.append(size)
                size = 0
        return res
        
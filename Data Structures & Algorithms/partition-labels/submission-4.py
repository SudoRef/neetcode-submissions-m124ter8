class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}

        res = []
        size,end = 0,0
        for i, ch in enumerate(s):
            last_idx[ch] = i
        for i, ch in enumerate(s):
            size+=1
            end = max(end, last_idx[ch])
            if i == end:
                res.append(size)
                size = 0
        return res


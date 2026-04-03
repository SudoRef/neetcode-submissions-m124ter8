class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prevEnd = intervals[0]
        res = []
        for start,end in intervals[1:]:
            if start <= prevEnd[1]:
                prevEnd[1] = max(end, prevEnd[1])
            else:
                res.append(prevEnd)
                prevEnd = [start,end]
        res.append(prevEnd)
        return res


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        res = 0
        for i in intervals[1:]:
            if prev_end > i[0]:
                res+=1
                prev_end = min(prev_end, i[1])
            else:
                prev_end = i[1]
        return res
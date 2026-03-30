"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i : i.start)
        output = [[intervals[0].start, intervals[0].end]]

        for i in range(1,len(intervals)):
            interval = intervals[i]
            start = interval.start
            end = interval.end
            lastEnd = output[-1][1]
            if start < lastEnd:
                return False
            output.append([start,end])
        return True
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        if len(intervals) < 2:
            return True
        prev_end = intervals[0].end
        for i in intervals[1:]:
            s = i.start
            e = i.end
            if s < prev_end:
                return False
            prev_end = e
        return True
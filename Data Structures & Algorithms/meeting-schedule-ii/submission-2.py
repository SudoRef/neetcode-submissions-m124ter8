"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i:i.start)
        ans = []
        if not intervals:
            return 0
        heapq.heappush(ans,intervals[0].end)

        for i in intervals[1:]:
            if ans[0] <= i.start:
                heapq.heappop(ans)
            heapq.heappush(ans, i.end)
        return len(ans)
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i: i.start)
        if not intervals:
            return 0
        min_heap = [intervals[0].end]
        for i in intervals[1:]:
            if i.start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,i.end)
        return len(min_heap)

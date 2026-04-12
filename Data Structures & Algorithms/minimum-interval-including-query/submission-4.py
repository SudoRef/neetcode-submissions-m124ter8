class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        i = 0
        res = {}
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0]<=q:
                start,end = intervals[i][0],intervals[i][1]
                heapq.heappush(min_heap, ((end - start + 1),end))
                i+=1
            while min_heap and q > min_heap[0][1]:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1
        return [res[q] for q in queries]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = [(0,0)]
        visited = set()
        res = 0
        while min_heap:
            curr, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            res+=curr
            visited.add(i)

            for j in range(len(points)):
                if j not in visited:
                    calc_val = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(min_heap, (calc_val, j))
        return res
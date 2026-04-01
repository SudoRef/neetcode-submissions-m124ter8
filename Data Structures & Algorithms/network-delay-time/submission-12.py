class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for ui,vi,ti in times:
            adj[ui].append((vi,ti))
        min_heap = [(0,k)]
        visited = set()
        res = -1
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            res = time

            for vi,time2 in adj[node]:
                if vi not in visited:
                    heapq.heappush(min_heap, (time + time2, vi))
        return res if len(visited) == n else -1

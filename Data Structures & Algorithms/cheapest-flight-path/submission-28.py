class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)
        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))
        min_heap = [(0,-1,src)]
        min_stops = [float("inf")] * n
        res = -1
        while min_heap:
            price_1, stops, from_i = heapq.heappop(min_heap)
            if dst == from_i:
                res = price_1
                break
            if stops == k:
                continue
            min_stops[from_i] = stops
            
            for to_i,price_2 in adj[from_i]:
                if stops + 1 < min_stops[to_i]:
                    heapq.heappush(min_heap, (price_1 + price_2, stops + 1, to_i))
        return res


        
    
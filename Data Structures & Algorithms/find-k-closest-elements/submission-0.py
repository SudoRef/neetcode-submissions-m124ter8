class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        for n in arr:
            val = abs(n - x)
            heapq.heappush(min_heap, (-val,-n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = sorted([-i for s,i in min_heap])
        return res
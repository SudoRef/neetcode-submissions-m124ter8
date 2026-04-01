class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        cnt = Counter(hand)
        keys = list(cnt.keys())
        heapq.heapify(keys)

        while keys:
            start = keys[0]
            if cnt[start] == 0:
                heapq.heappop(keys)
                continue
            for i in range(start, start + groupSize):
                if i not in cnt or cnt[i] == 0:
                    return False
                cnt[i]-=1
                if cnt[i] == 0:
                    heapq.heappop(keys)
        return True
                
            
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1
        q = deque()
        q.append(("0000",0))

        while q:
            comb,steps = q.popleft()
            if comb == target:
                return steps
            for i in range(4):
                val = int(comb[i])
                prev = val-1
                if prev < 0:
                    prev = 9
                nxt = val+1
                if nxt > 9:
                    nxt = 0
                n_comb1 = comb[:i] + str(prev) + comb[i+1:]
                n_comb2 = comb[:i] + str(nxt) + comb[i+1:]
                if n_comb1 not in visited:
                    visited.add(n_comb1)
                    q.append((n_comb1, steps+1))
                if n_comb2 not in visited:
                    visited.add(n_comb2)
                    q.append((n_comb2, steps+1))
        return -1
                    


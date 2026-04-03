class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for ch in t:
            t_map[ch]+=1
        have = len(t_map)
        need = 0
        arr = [-1,-1]
        l = 0
        min_len = float("inf")

        for r, ch in enumerate(s):
            s_map[ch]+=1
            if ch in t_map and t_map[ch] == s_map[ch]:
                need+=1
            while need == have:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    arr = [l, r]
                val = s[l]
                if val in t_map and s_map[val] == t_map[val]:
                    need-=1
                s_map[val] -= 1
                if s_map[val] == 0:
                    del s_map[val]
                l+=1
        return s[arr[0]:arr[1]+1] if min_len != float("inf") else ""
                
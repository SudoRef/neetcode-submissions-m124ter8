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
        curr_min = float("inf")

        for r in range(len(s)):
            ch = s[r]
            s_map[ch]+=1
            
            if ch in t_map and s_map[ch] == t_map[ch]:
                need+=1
            while need == have:
                if r - l + 1 < curr_min:
                    curr_min = r - l + 1
                    arr = [l,r]
                val = s[l]
                
                if val in t_map and s_map[val] == t_map[val]:
                    need-=1
                s_map[val]-=1
                if s_map[val] == 0:
                    del s_map[val]
                l+=1
        return s[arr[0]:arr[1]+1] if curr_min != float("inf") else ""
                
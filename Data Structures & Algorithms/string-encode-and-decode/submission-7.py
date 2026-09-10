class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res+=str(l)+"%"+s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            length = 0
            r = idx
            l = idx
            while s[r] != "%":
                r+=1
            
            length = int(s[l:r])
            
            word = s[r+1:r+length+1]
            res.append(word)
            idx = r+length+1
        return res



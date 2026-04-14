class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            cnt = 0
            curr = i
            while curr != 0:
                curr = curr & (curr - 1)
                cnt+=1
            res[i] = cnt
        return res

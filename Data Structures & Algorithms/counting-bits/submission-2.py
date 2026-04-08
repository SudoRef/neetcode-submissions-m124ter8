class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            curr = i
            cnt= 0
            while curr:
                curr = curr & (curr - 1)
                cnt+=1
            res[i] = cnt

        return res
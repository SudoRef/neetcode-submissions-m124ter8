class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n != 1:
            curr = n
            res = 0
            while curr:
                res += (curr % 10) * (curr % 10)
                curr //= 10
            n = res
            if n in s:
                return False
            s.add(n)
        return True

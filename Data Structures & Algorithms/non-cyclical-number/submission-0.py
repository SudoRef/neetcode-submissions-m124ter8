class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n != 1:
            new_n = 0
            while n:
                new_n += (n % 10) * (n % 10)
                n = n // 10
            n = new_n
            if n in s:
                return False
            s.add(n)
        return True
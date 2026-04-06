class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n != 1:
            new_n = 0
            while n:
                new_n += (n % 10) * (n % 10)
                n = n // 10
            if new_n in s:
                return False
            n = new_n
            s.add(new_n)
        return True

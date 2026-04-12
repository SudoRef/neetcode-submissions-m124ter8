class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n != 1:
            curr = n
            num = 0
            while curr:
                num += (curr % 10) * (curr % 10)
                curr//=10
            if num in s:
                return False
            s.add(num)
            n = num
        return True
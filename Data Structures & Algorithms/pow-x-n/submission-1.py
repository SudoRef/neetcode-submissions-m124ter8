import functools

class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        
        @functools.cache
        def helper(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = helper(x * x, n // 2)
            return res if n % 2 == 0 else x * res
        res = helper(x,abs(n))
        return res if n >= 0 else 1/res
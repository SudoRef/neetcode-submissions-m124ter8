class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(s):
            res = 0
            for i in range(len(s)):
                num = int(s[i])
                res+=num
                if i != len(s)-1:
                    res*=10
            return res
        def convertResult(n):
            if n ==0:
                return "0"
            s = ""
            while n:
                rem = n % 10
                n = n // 10
                s+=str(rem)
            
            return s[::-1]

        n1 = convert(num1)
        n2 = convert(num2)

        return convertResult(n1 * n2)
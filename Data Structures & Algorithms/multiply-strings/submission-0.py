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
        n1 = convert(num1)
        n2 = convert(num2)
        return str(n1 * n2)
        
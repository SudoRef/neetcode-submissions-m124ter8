class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        for i in range(len(digits)-1,-1,-1):
            val = digits[i]+rem
            digits[i] = val % 10
            rem = val // 10
        if rem:
            return [rem] + digits
        return digits
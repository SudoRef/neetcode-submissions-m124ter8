class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        for i in range(len(digits)-1,-1,-1):
            n = digits[i]
            n = n + rem
            digits[i] = n % 10
            rem = n // 10
        if rem:
            return [rem] + digits
        return digits
        
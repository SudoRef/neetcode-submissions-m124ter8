class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        for i in range(len(digits)-1,-1,-1):
            if rem:
                digits[i]+=1
                rem = digits[i] // 10
                digits[i] %= 10
        if rem:
            return [1] + digits
        return digits

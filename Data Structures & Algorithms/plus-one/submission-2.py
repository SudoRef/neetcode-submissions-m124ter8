class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        res = []
        for i in range(len(digits)-1,-1,-1):
            curr = digits[i] + rem
            res.append(curr % 10)
            rem = curr // 10
        res.reverse()
        if rem:
            return [rem] + res
        return res
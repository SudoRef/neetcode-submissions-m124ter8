class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        my_set = set()
        m = float("inf")
        for n in nums:
            my_set.add(n)
            m = min(m,n)
        if m > 1:
            return 1
        while True:
            if m not in my_set and m > 0:
                return m
            m+=1
        return -1
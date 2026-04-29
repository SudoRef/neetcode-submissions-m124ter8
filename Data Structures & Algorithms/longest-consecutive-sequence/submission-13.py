class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in nums:
            num = n
            if num-1 not in s:
                curr = 1
                while num + 1 in s:
                    curr+=1
                    num+=1
                res = max(res, curr)
        return res
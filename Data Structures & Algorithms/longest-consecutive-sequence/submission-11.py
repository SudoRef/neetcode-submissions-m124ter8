class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        if len(nums) == 0:
            return 0
        ans = 0
        for n in nums:
            curr = 1
            if n - 1 in my_set:
                continue
            while n + 1 in my_set:
                curr+=1
                n+=1
            ans = max(ans, curr)
        return ans
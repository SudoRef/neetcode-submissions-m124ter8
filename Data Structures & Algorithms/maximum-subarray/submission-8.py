class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float("-inf")
        ans = float("-inf")
        for n in nums:
            curr = max(n, curr + n)
            ans = max(curr, ans)
        return ans
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(curr, i):
            if i == len(nums):
                return curr == target
            if i >= len(nums):
                return 0
            if (curr,i) in dp:
                return dp[(curr,i)]
            res = dfs(curr+nums[i],i+1)
            if i < len(nums):
                res+=dfs(curr-nums[i],i+1)
            dp[(curr,i)] = res
            return res
        return dfs(0,0)

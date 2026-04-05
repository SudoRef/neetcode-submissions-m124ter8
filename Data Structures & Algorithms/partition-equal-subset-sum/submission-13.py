class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            new_dp = set()
            for t in dp:
                new_dp.add(nums[i] + t)
                new_dp.add(t)
            dp = new_dp
        return target in dp
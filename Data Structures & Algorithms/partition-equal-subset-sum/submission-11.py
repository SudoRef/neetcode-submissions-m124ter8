class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)

        target = sum(nums) //2

        for n in nums:
            new_dp = set()
            for t in dp:
                new_dp.add(t + n)
                new_dp.add(t)
            dp = new_dp
        return target in dp
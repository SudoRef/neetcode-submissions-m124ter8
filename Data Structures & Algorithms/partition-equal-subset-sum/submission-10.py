class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            st = set()
            for t in dp:
                st.add(nums[i] + t)
                st.add(t)
            dp = st
        return target in dp
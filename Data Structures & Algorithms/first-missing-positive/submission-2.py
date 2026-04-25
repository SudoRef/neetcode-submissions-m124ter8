class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        for i in range(len(nums)):

            while 0 <= nums[i] < N and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[correct_idx],nums[i] = nums[i], nums[correct_idx]
        
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

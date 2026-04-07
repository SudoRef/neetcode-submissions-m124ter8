class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        curr = 1
        res = 1
        n = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                curr += 1
                if curr > res:
                    n = nums[i]
                    res = curr
            else:
                curr = 1
        return n
            

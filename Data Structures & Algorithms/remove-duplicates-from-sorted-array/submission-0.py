class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != curr:
                nums[ptr] = nums[i]
                curr = nums[i]
                ptr+=1
        return ptr
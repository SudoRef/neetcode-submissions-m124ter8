class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = two = 0
        
        
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[zero] = nums[zero],nums[i]
                zero+=1
        for i in range(len(nums)):
            if nums[i] != 1:
                nums[i],nums[one] = nums[one],nums[i]
                one+=1
        for i in range(len(nums)):
            if nums[i] != 2:
                nums[i],nums[two] = nums[two],nums[i]
                two+=1 


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        target = len(nums) // 3
        res = []
        for k,v in cnt.items():
            if v > target:
                res.append(k)
        return res

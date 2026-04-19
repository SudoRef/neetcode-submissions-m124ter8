class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can = defaultdict(int)

        for n in nums:
            can[n]+=1
            if len(can) <= 2:
                continue
            
            new_count = defaultdict(int)
            for k,c in can.items():
                if c > 1:
                    new_count[k] = c - 1
            can = new_count
        target = len(nums) // 3
        res = []
        for k, v in can.items():
            if nums.count(k) > target:
                res.append(k)
        return res
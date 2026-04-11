class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_idx = {}
        for i in range(len(nums)):
            v = nums[i]
            if v in last_idx:
                if abs(i - last_idx[v]) <= k:
                    return True
            last_idx[v] = i
        return False
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        curr = 0
        for n in nums:
            curr+=n
            ans+=cnt[curr - k]
            cnt[curr]+=1
        return ans

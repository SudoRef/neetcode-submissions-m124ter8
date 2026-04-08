class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l,r = 0, len(people) - 1
        while l <= r:
            curr = 0
            curr+=people[r]
            r-=1
            if curr + people[l] <= limit:
                curr+=people[l]
                l+=1
            res+=1
        return res
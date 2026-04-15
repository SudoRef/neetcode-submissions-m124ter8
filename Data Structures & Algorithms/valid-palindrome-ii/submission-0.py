class Solution:
    def validPalindrome(self, s: str) -> bool:
        k = 1
        l,r = 0,len(s)-1
        def isPal(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                r-=1
                l+=1
            return True

        while l < r:
            if s[l] == s[r]:
                r-=1
                l+=1
            else:
                if isPal(l+1,r) or isPal(l,r-1):
                    return True
                return False
        return True
        
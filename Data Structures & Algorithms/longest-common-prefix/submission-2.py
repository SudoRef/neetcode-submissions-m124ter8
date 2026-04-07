class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        res = []
        for i in range(len(first)):
            ch = first[i]
            for s in strs[1:]:
                if not s:
                    return ""
                if i >= len(s) or s[i] != ch:
                    return "".join(res)
            res.append(ch)
        return "".join(res)
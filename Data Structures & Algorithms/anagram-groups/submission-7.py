class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for s in strs:
            arr = list(s)
            arr.sort()
            new_s = "".join(arr)
            freq[new_s].append(s)
        return list(freq.values())

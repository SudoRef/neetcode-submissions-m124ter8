class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        my_map = {}
        for i in range(len(order)):
            ch = order[i]
            my_map[ch] = i
        def compare(w1,w2):
            i,j = 0,0
            while i < len(w1) and j < len(w2) and w1[i]==w2[j]:
                i+=1
                j+=1
            if i >= len(w1):
                return True
            if j < len(w2) and my_map[w1[i]] < my_map[w2[j]]:
                return True
            return False
        for i in range(1,len(words)):
            w1 = words[i-1]
            w2 = words[i]
            if not compare(w1,w2):
                return False
        return True

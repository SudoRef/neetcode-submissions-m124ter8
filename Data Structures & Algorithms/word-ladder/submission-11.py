class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        w_list = set(wordList)
        visited = set(beginWord)
        q = deque()
        q.append((1,beginWord))

        while q:
            curr, w = q.popleft()
            if w == endWord:
                return curr
            for i in range(len(w)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = w[:i] + ch + w[i+1:]
                    if new_word in w_list and new_word not in visited:
                        q.append((curr+1, new_word))
                        visited.add(new_word)
        return 0
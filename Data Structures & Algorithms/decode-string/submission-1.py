class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        for ch in s:
            if ch == ']':
                curr = []
                while stack and stack[-1] != '[':
                    curr.append(stack.pop())
                stack.pop()
                n = []
                while stack and stack[-1].isnumeric():
                    n.append(stack.pop())
                n.reverse()   
                num = int("".join(n))
                curr.reverse()
                s = "".join(curr)
                for i in range(num):
                    stack.append(s)
            else:
                stack.append(ch)
        return "".join(stack)



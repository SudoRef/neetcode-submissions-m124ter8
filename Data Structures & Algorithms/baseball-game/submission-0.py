class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == "C":
                stack.pop()
            elif o == "D":
                v1 = stack[-1]
                stack.append(v1 * 2)
            elif o == "+":
                v1 = stack[-1]
                v2 = stack[-2]
                stack.append(v1 + v2)
            else:
                stack.append(int(o))
        return sum(stack)
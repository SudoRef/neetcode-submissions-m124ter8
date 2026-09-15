class Solution:
    def simplifyPath(self, path: str) -> str:
        new_p = path.split("/")
        stack = []
        
        for ch in new_p:
            if ch:
                if ch == "..":
                    if stack:
                        stack.pop()
                    else:
                        continue
                elif ch == ".":
                    continue
                else:
                    stack.append(ch)
        return "/" + "/".join(stack)

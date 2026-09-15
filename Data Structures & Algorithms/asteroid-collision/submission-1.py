class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if -a > stack[-1]:
                    stack.pop()
                    
                elif -a == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)
        return stack
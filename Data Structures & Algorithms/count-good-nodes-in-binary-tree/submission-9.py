# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(prev, node):
            nonlocal res
            if not node:
                return
            if node.val >= prev:
                res+=1
            prev = max(prev,node.val)
            dfs(prev, node.left)
            dfs(prev, node.right)
        dfs(float("-inf"), root)
        return res

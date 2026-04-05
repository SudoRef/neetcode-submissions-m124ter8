# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        def dfs(node,p,q):
            nonlocal res
            if not node:
                return None
            if node.val < p.val and node.val < q.val:
                return dfs(node.right, p, q)
            elif node.val > p.val and node.val > q.val:
                return dfs(node.left,p,q)
            else:
                res = node
            return node
        dfs(root,p,q)
        return res

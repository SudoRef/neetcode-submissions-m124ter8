# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def is_leaf(node):
            return node.right == None and node.left == None and node.val == target
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if node.left and is_leaf(node.left):
                node.left = None
            if node.right and is_leaf(node.right):
                node.right = None
        dfs(root)
        if is_leaf(root):
            return None
        return root
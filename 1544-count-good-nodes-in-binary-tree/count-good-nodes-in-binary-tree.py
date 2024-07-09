# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, m):
            if not root: return 0
            m = max(root.val, m)
            return (root.val >= m) + dfs(root.left, m) + dfs(root.right, m)

        return dfs(root, root.val)
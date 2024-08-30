class Solution:
    def deleteNode(self, root: TreeNode, key: int):
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            cur = root.right
            while cur.left: cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root
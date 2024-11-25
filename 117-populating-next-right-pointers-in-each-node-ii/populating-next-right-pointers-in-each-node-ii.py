"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                cur.next = q[0] if i < size - 1 else None

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root
from collections import deque

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        queue = deque([root])

        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return root

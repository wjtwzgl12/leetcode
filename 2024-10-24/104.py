from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        queue = deque([root])
        d = 0

        while queue:
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            d += 1
        
        return d

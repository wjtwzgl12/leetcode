class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = None

        def in_order(node):
            if not node or self.result is not None:
                return

            in_order(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            in_order(node.right)
        
        in_order(root)
        return self.result

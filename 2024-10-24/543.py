# 定义树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0  
        def depth(node):
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)
            

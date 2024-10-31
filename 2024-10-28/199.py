class Solution:
    def rightSideView(self, root):
        result = []

        def dfs(node, level):
            if not node:
                return
            if level == len(result):
                result.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result

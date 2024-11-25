class Solution:
    def pathSum(self, root, targetSum):
        prefix_sums = {0: 1} 
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix_sums.get(curr_sum - targetSum, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            prefix_sums[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)

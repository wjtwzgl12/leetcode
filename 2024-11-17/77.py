class Solution:
    def combine(self, n, k):
        def backtrack(start, path):
            # 如果路径长度等于 k，保存当前组合
            if len(path) == k:
                result.append(path[:])
                return
            
            # 从当前数字开始，尝试所有可能的选择
            for i in range(start, n + 1):
                # 做选择
                path.append(i)
                
                # 递归处理剩余数字
                backtrack(i + 1, path)
                
                # 撤销选择
                path.pop()

        result = []
        backtrack(1, [])
        return result


# class Solution:
#     def combine(self, n, k):
#         dp = [[] for _ in range(k + 1)]
#         dp[0] = [[]]  # 初始状态，空组合

#         for num in range(1, n + 1):
#             for j in range(k, 0, -1):
#                 dp[j] += [comb + [num] for comb in dp[j - 1]]

#         return dp[k]

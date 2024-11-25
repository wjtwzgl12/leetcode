class Solution:
    def permute(self, nums):
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])  
                return
            
            for i in range(len(nums)):
                # 如果数字已经被用过，跳过
                if used[i]:
                    continue
                
                # 做选择：将数字加入路径
                path.append(nums[i])
                used[i] = True
                
                # 递归到下一层
                backtrack(path)
                
                # 撤销选择：回退
                path.pop()
                used[i] = False

        result = []
        used = [False] * len(nums)  # 初始化所有数字都未使用
        backtrack([])
        return result

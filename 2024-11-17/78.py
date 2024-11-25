class Solution:
    def subsets(self, nums):
        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        result = []
        backtrack(0, [])
        return result
    
    # class Solution:
    # def subsets(self, nums):
    #     result = [[]]  # 初始只有空集
    #     for num in nums:
    #         # 将当前数字加入所有现有子集，生成新子集
    #         result += [curr + [num] for curr in result]
    #     return result



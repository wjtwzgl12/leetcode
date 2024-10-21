class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, num in enumerate(nums):
            comple = target - num 
            if comple in hash_map:
                return [hash_map[comple], i]
            hash_map[num] = i 
        return []

if __name__ == "__main__":
    solution = Solution()
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        max_num = max(nums)

        seen = [False] * (max_num + 1)
        for num in nums:
            if 1 <= num <= max_num:
                seen[num] = True
        for i in range(1, max_num + 1):
            if not seen[i]:
                return i

        return max_num + 1
    
if __name__ == "__main__":
    solution = Solution()        
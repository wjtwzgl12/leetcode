class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        
        k = k % n        
        def reverse(lst, start, end):
            while start < end:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1

        reverse(nums, 0, n-1)

        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)

if __name__ == "__main__":
    solution = Solution()
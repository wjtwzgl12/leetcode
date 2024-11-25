class Solution:
    def findMin(self, nums):
        def binary_search(left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid)
        
        return binary_search(0, len(nums) - 1)

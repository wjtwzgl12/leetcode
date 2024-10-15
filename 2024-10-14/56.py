class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or len(intervals) == 1:
            return intervals

        intervals_sorted = sorted(intervals, key=lambda interval: interval[0])
        merged = [intervals_sorted[0]]

        for current in intervals_sorted[1:]:
            last = merged[-1] 

            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged
    
if __name__ == "__main__":
    solution = Solution()
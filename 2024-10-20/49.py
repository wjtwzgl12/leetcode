class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        map = defaultdict(list) 
        for s in strs:
            sorted_s = ''.join(sorted(s))
            map[sorted_s].append(s)  
        return list(map.values())

if __name__ == "__main__":
    solution = Solution()
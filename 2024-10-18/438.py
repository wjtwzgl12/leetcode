class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        p_len = len(p)
        s_len = len(s)
        
        if p_len > s_len:
            return result
        
        p_count = {}
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1
        
        for i in range(s_len - p_len + 1):
            window = s[i:i+p_len]
            window_count = {}
            for char in window:
                window_count[char] = window_count.get(char, 0) + 1

            if window_count == p_count:
                result.append(i)
        
        return result

if __name__ == "__main__":
    solution = Solution()
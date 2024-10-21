class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        p_len = len(s1)
        s_len = len(s2)

        if p_len > s_len:
            return False

        p_count = {}
        for char in s1:
            p_count[char] = p_count.get(char, 0) + 1

        window_count = {}
        left = 0
        
        for right in range(s_len):
            char = s2[right]
            window_count[char] = window_count.get(char, 0) + 1

            if right - left + 1 > p_len:
                left_char = s2[left]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]
                left += 1

            if right - left + 1 == p_len:
                if window_count == p_count:
                    return True
        
        return False

if __name__ == "__main__":
    solution = Solution()
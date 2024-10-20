class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_length = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                current_length = j - i + 1
                if current_length > max_length:
                    max_length = current_length

        return max_length

if __name__ == "__main__":
    solution = Solution()


################滑动窗口

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_length = 0
        left = 0
        char_set = set()

        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length

        return max_length

if __name__ == "__main__":
    solution = Solution()
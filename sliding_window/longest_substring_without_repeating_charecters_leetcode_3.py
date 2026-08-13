class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        seen = {}
        max_length = 0

        for right in range(len(s)):

            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)

            seen[s[right]] = right

            length = right - left + 1
            max_length = max(max_length, length)

        return max_length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = right = maxLen = 0
        seen = {}

        while right < n:
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            maxLen = max(maxLen, right - left + 1)
            right += 1
        
        return maxLen

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = left = right = max_freq = 0
        n = len(s)
        count = defaultdict(int)
        
        while right < n:
            count[s[right]] += 1
            max_freq = max(max_freq,count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, -left+right+1)
            right += 1

        return max_length

            

        
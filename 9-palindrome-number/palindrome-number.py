class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return ''.join(s) == ''.join(s[::-1])
        
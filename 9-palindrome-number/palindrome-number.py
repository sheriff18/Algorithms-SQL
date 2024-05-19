class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reverse = 0
        
        while x != 0:
            last_digit = x % 10
            reverse = reverse * 10 + last_digit
            x = x // 10
        
        return reverse == original


       
        
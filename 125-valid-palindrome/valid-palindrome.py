class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string by keeping only alphanumeric characters and converting to lowercase
        cleaned_string = ''
        for char in s:
            if char.isalnum():
                cleaned_string += char.lower()
        
        # Define a nested helper function for recursion
        def check(i, cleaned_string):
            n = len(cleaned_string)
            if i >= n // 2:
                return True
            if cleaned_string[i] != cleaned_string[n - 1 - i]:
                return False
            return check(i + 1, cleaned_string)
        
        # Start the recursive check from the first character
        return check(0, cleaned_string)




            


        
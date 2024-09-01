class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for character in s:
            if character == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(character)
        return ''.join(stack)
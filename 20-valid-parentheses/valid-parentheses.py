class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}

        stack = []

        for br in s:
            if br in brackets:
                stack.append(br)
            else:
                if not stack or br !=  brackets[stack.pop()]:
                    return False
        return len(stack) == 0
            


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack = []
        res = set()
        last_occurrence = {char: i for i, char in enumerate(s)}

        for i in range(n):
            char = s[i]
            
            # If the character is already in the result, continue
            if char in res:
                continue

            # Ensure the stack is not empty and we can pop the top of the stack
            while stack and stack[-1] > char and i < last_occurrence[stack[-1]]:
                res.remove(stack.pop())

            stack.append(char)
            res.add(char)

        return ''.join(stack)


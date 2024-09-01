class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for a in logs:
            if a == '../':
                if stack:
                    stack.pop()
                    
            elif a != './':
                stack.append(a)
            
        return len(stack) 
        
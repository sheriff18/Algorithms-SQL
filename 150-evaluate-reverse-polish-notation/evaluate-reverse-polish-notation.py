class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+', '-', '*', '/'}
        stack = []
        
        for val in tokens:
            if val in operations:
                x = stack.pop()
                y = stack.pop()
                
                if val == '+':
                    stack.append(y + x)
                elif val == '-':
                    stack.append(y - x)
                elif val == '*':
                    stack.append(y * x)
                elif val == '/':
                    # Use integer division with truncation towards zero
                    stack.append(int(y / x))
            else:
                stack.append(int(val))
        
        # Return the final result, which is the only element in the stack
        return stack[-1]

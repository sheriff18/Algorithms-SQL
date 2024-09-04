class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        s = path.split('/')

        for component in s:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        
        return '/' + '/'.join(stack)

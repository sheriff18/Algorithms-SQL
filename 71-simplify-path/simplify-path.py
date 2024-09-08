class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        stack = []
        
        for w in s:
            if w == '' or w == '.':
                continue
            elif w == '..':
                if stack:

                    stack.pop()
            else:stack.append(w)
        
        return '/' + '/'.join(stack)

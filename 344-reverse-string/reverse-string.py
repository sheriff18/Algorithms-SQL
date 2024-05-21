class Solution:
    def reverseString(self, s: List[str]) -> None:

        n = len(s)
        def rev(i):
            if i >= n//2:
                return
            s[i], s[n-i-1] = s[n-i-1],s[i]
            rev(i+1)
        rev(0)

        return s

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        hashing = {'a':-1,'b':-1,'c':-1} 

        for i in range(n):
            hashing[s[i]] = i
            
        
            if -1 not in hashing.values():

                cnt += 1 + min(hashing.values())

        return cnt 

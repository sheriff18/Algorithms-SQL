from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        target = Counter(p)
        window = Counter(s[:len(p)])
        if window == target:
            result.append(0)

        for i in range(len(p),len(s)):
            
            if window[s[i-len(p)]] == 0:
                del window[s[i-len(p)]] 
            else:
                window[s[i-len(p)]] -= 1
            
            window[s[i]] += 1


            
            

            if window == target:
                result.append(i-len(p)+1)

        
        
        return result

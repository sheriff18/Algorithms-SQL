from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = Counter(s2[:len(s1)])
        s = window
        
        if target == window:
            return True
        
        for i in range(len(s1),len(s2)):
            if window[s2[i-len(s1)]] == 1:
                del window[s2[i - len(s1)]]
            else:
                window[s2[i - len(s1)]] -= 1
            
            window[s2[i]] += 1
            


            if window == target:
                return True
        
        return False


        

from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        
        if n % 2 != 0:
            # If the number of players is odd, pairing is not possible
            return -1
        
        skill.sort()
        
        i, j = 0, n - 1
        target_sum = skill[i] + skill[j]
        pairs = []

        while i < j:
            if skill[i] + skill[j] != target_sum:
                return -1
            pairs.append((skill[i], skill[j]))
            i += 1
            j -= 1
        
        total = sum(a * b for a, b in pairs)
        return total

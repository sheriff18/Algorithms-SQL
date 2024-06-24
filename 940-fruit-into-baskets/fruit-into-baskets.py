from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = right = 0
        counter = {}
        n = len(fruits)
        maxLen = 0

        while right < n:
            if fruits[right] in counter:
                counter[fruits[right]] += 1
            else:
                counter[fruits[right]] = 1
            

            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1


        return maxLen

       

        
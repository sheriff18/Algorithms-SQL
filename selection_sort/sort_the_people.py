https://leetcode.com/problems/sort-the-people/submissions/1077579648/


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        
    
        for i in range(n - 1):
            max_index = i
            for j in range(i + 1, n):

                if heights[j] > heights[max_index]:

                    max_index = j

        # Swap names and heights
            names[i], names[max_index] = names[max_index], names[i]
            heights[i], heights[max_index] = heights[max_index], heights[i]
        return names

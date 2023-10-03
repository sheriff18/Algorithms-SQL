https://leetcode.com/problems/sort-the-people/description/


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ## Using insertion sort
        n = len(heights)
        for i in range(1,n):
            j = i
            while j > 0 and heights[j-1] < heights[j]:
                names[j-1], names[j] = names[j], names[j-1]
                heights[j-1], heights[j] = heights[j], heights[j-1]
                j -= 1
                
        return names

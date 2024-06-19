class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        n = len(people)
        left, right = 0 , n-1
        boat = 0
        people.sort()

        while left <= right:
            total = people[left] + people[right]
            if total <= limit:
                boat += 1
                right -= 1
                left += 1
            elif total > limit:
                boat += 1
                right -= 1
            
        return boat

            
        
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hopOffandOn = []

        for count, start, end in trips:
            hopOffandOn.append((start, count))  # Add passengers at the start location
            hopOffandOn.append((end, -count))   # Remove passengers at the end location

        # Sort the events primarily by location. If they have same location, then drop off (-count) comes before count
        hopOffandOn.sort(key=lambda x: (x[0],x[1]))
        
        prefix = 0
        for location, passenger_change in hopOffandOn:
            prefix += passenger_change  # Update the number of passengers in the car

            if prefix > capacity:
                return False  # If the number of passengers exceeds capacity, return False

        return True  

         

        
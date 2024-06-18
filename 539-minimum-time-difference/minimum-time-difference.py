from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertToMinutes(time):
            hours, mins = map(int, time.split(':'))
            return hours * 60 + mins

        # Convert all time points to minutes and sort them
        arr = sorted([convertToMinutes(time) for time in timePoints])
        n = len(arr)
        min_time = float('inf')

        # Find the minimum difference between consecutive time points
        for i in range(n - 1):
            mini = arr[i + 1] - arr[i]
            min_time = min(mini, min_time)

        # Check the difference between the last and first time points (wrapping around midnight)
        wrap_around_diff = 1440 + arr[0] - arr[-1]
        min_time = min(wrap_around_diff, min_time)

        return min_time


         
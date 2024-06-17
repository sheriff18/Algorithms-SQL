
https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
#User function Template for python3

class Solution:
    def findTwoElement(self, arr, n): 
        hashing = [0] * (n + 1)  # Initialize hashing array of size n+1

        for i in range(n):
            hashing[arr[i]] += 1  # Count occurrences of each element in the array

        # Initialize variables for missing and repeating numbers
        missing = repeating = -1

        for i in range(1, n + 1):
            if hashing[i] == 0:
                missing = i  # Missing number has zero occurrences
            elif hashing[i] == 2:
                repeating = i  # Repeating number has two occurrences

        return (repeating, missing)  # Return the result as a tuple

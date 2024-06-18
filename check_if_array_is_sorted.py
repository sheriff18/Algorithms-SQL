https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

class Solution:
    def arraySortedOrNot(self, arr, n):
        i, j = 0, 1
        
        while i < j and j < n:
            if arr[i] > arr[j]:
                return 0
            else:
                i += 1
                j += 1
        return 1

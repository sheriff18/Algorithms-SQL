class Solution:
    def sortSentence(self, s: str) -> str:
        # Find an array of words
        arr = s.split()

        # Sort by the last letter
        arr.sort(key = lambda x:x[-1])

        # Remove the last words

        sorted_arr = [num[:-1] for num in arr ]

        # Return a string of sorted_arr

        return ' '.join(sorted_arr)
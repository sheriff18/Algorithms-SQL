class Solution:
    def generate_row(self, numRows: int) -> List[int]:
        res = 1
        ans = [1]
        for i in range(1, numRows):
            res *= (numRows - i)
            res //= i
            ans.append(res)
        return ans

    def generate(self, numRows: int) -> List[List[int]]:
        mylist = []
        for i in range(1, numRows + 1):
            mylist.append(self.generate_row(i))
        return mylist
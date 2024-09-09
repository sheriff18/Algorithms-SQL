class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                
                res[stack[-1]] = i - stack[-1]
                stack.pop()


            stack.append(i)

        return res




            


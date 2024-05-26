class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for i in range(len(points)):
            distance = (points[i][0]**2 + points[i][1]**2)**0.5
            arr.append([distance,points[i]])

        arr.sort()
        res = []
        for i in range(k):
            res.append(arr[i][1])

        return res


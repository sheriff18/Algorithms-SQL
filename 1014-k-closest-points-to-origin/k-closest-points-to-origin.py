class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []
           
        res = []

        for i in range(len(points)):

            distance =  math.sqrt( ( points[i][0] ) **2 + ( points[i][1] ) **2  )
            distances.append([distance,points[i]])
        
        distances.sort()
            
        
        for i in range(k):
            res.append(distances[i][1])

        
        return res
        


        
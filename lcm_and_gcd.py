https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1

class Solution:
    def gcd(self,A,B):
        while A>0 and B>0:
            
            if A > B:
                A = A % B
            else:
                B = B % A
        
        if A == 0:
            return B
        else: return A
        
    def lcmAndGcd(self, A , B):
        num = []
        num_gcd = self.gcd(A,B)
        num_lcm = A*B//self.gcd(A,B)
        num.append(num_lcm)
        num.append(num_gcd)
        return num
        # code here 

#User function Template for python3
from math import floor, sqrt
class Solution:
    def countFactors (self, n):
        count = 0
        for i in range(1, floor(sqrt(n)) + 1):
            if(n % i == 0):
                count += 2
            if(i * i == n):
                count -= 1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.countFactors(N))
# } Driver Code Ends
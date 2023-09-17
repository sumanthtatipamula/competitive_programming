#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def print_divisors(self, N):
       i = 1
       while(i * i <= N):
           if(N % i == 0):
               print(i, end = ' ')
           i += 1
       i -= 1
       while(i >= 1):
           if(N % i == 0 and i * i != N):
               print(N // i, end = ' ')
           i -= 1

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        ob.print_divisors(N)
        print()
# } Driver Code Ends
#User function Template for python3

from math import floor, sqrt
class Solution:
    def isPrime(self, num):
        if(num <= 1):
            return False
        if(num == 2 or num == 3):
            return True
        if(num % 2 == 0 or num % 3 == 0):
            return False
        i = 5
        while(i * i  <= num):
            if(num % i == 0 or num % (i + 2) == 0):
                return False
            i += 6
        return True
	def threeDivisors(self, query, q):
	    result = []
	    for n in query:
	        count = 0
		    for i in range(2, floor(sqrt(n)) + 1):
		        if(self.isPrime(i)):
		            count += 1
            result.append(count)
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		q = int(input())
		query = []
		for _ in range(q):
			query.append(int(input()))
		
		ob = Solution()
		ans = ob.threeDivisors(query,q)
		for a in ans:
			print(a)

# } Driver Code Ends
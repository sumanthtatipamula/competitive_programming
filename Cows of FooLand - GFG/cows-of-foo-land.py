#User function Template for python3

class Solution:
    def TotalAnimal(self, n):
        matrix = [[1, 1], [1, 0]]
        if n <= 1:
            return n
        result = self.findFib(matrix, n)
        return result[0][0]

    def findFib(self, matrix, n):
        if n == 1:
            return matrix
        tmp = self.findFib(matrix, n // 2)
        if n % 2 == 0:
            return self.multiply(tmp, tmp)
        else:
            return self.multiply(self.multiply(tmp, tmp), matrix)

    def multiply(self, a, b):
        result, mod = [[0, 0], [0, 0]], 10 ** 9 + 7
        result[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod
        result[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod
        result[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod
        result[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalAnimal(N)
		print(ans)
# } Driver Code Ends
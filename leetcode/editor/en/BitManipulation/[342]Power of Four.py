# Given an integer n, return true if it is a power of four. Otherwise, return 
# false. 
# 
#  An integer n is a power of four, if there exists an integer x such that n == 
# 4ˣ. 
# 
#  
#  Example 1: 
#  Input: n = 16
# Output: true
#  
#  Example 2: 
#  Input: n = 5
# Output: false
#  
#  Example 3: 
#  Input: n = 1
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  -2³¹ <= n <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you solve it without loops/recursion?
# 
#  Related Topics Math Bit Manipulation Recursion 👍 3239 👎 345


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0 or n == 2:
            return False
        return (n - 1) % 3 == 0 and ((n & n - 1) == 0)
        
# leetcode submit region end(Prohibit modification and deletion)

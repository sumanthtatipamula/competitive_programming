# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
#
#  Given two integers x and y, return the Hamming distance between them.
#
#
#  Example 1:
#
#
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are
# different.
#
#
#  Example 2:
#
#
# Input: x = 3, y = 1
# Output: 1
#
#
#
#  Constraints:
#
#
#  0 <= x, y <= 2³¹ - 1
#
#
#  Related Topics Bit Manipulation 👍 3688 👎 213


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, count = x ^ y, 0
        while x:
            x = x & (x - 1)
            count += 1
        return count


# leetcode submit region end(Prohibit modification and deletion)

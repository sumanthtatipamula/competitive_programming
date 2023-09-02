"""
You are given two 32-bit numbers N and M and two bit positions i and j.
Write a method to set all bits between i and j in N equal to M.
M becomes a substring of N locationed at and starting at j
"""


def replace_bits(n, m, i, j):
    m = m << i
    a, b = ~0 << j + 1, (1 << i) - 1
    n = n & (a | b)
    return m | n


print(replace_bits(15, 2, 1, 3))

---
title: Bit Manipulation Techniques
tags:
  - Basics
  - Bitmap
---

## Operators

- Binary AND
- Binary OR
- XOR
- Binary NOT
- Left Shift
- Right Shift

### Binary And &

| A | B | A AND B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 1       |

### Binary OR |

| A | B | A OR B |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |

### Binary XOR ^

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 0       |

### Binary Not ~

| A | NOT A |
|---|-------|
| 0 | 1     |
| 1 | 0     |

- For negative numbers, to get magnitude we need to perform 2's complement (flip and add 1)

```python
a = 0
print(~a)  # -1
a = 1
print(~b)  # -2
```

### Binary Left Shift

- When you apply the left shift operator, the bits in the binary representation of the left operand are shifted to the
  left by the number of positions specified by the right operand. This effectively multiplies the left operand by 2
  raised to the power of the right operand.
- a << b = a * 2 ^ b

### Binary Right Shift

- When you apply the right shift operator, the bits in the binary representation of the left operand are shifted to the
  right by the number of positions specified by the right operand. This effectively performs integer division by 2
  raised to the power of the right operand.
- a >> b = a / 2 ^ b

## Useful Expressions

1. Finding if a number is even or odd

  ```python
    a = int(input())
if a & 1:
    print("Odd")
else:
    print("Even")
  ```

2. ith bit of a number

  ```python
    num = num >> pos & 1
  ```

3. Clear ith bit of a number

  ```python
    num = num & ~(1 << pos)
  ```

4. Set ith bit of a number

  ```python
    num = num | (1 << pos)
  ```

5. Update ith bit of a number

  ```python
    num = num & ~(1 << pos)
    num = num | new_val << pos
  ```

6. Clear last i bits

  ```python
    num = num & (~0 << pos)
  ```

7. Clear bits between i and j

  ```python
    a = ~0 << j + 1
    b = (1 << i) - 1
    num = num & (a | b)
  ```

## Summary

```python
class BitOperations:
    def __init__(self, num):
        self.num = num

    def getithbit(self, pos):
        return self.num >> pos & 1

    def clearithbit(self, pos):
        # self.num = self.num ^ (1 << self.pos)
        self.num = self.num & ~(1 << pos)
        return self.num

    def setithbit(self, pos):
        self.num = self.num | (1 << pos)
        return self.num

    def updateith(self, pos, new_val):
        self.clearithbit(pos)
        self.num = self.num | new_val << pos
        return self.num

    def clear_last_ith_bits(self, pos):
        self.num = self.num & (~0 << pos)
        return self.num

    def clear_bits_in_range(self, i, j):
        a = ~0 << j + 1
        b = (1 << i) - 1
        self.num = self.num & (a | b)
        return self.num
```

## Problems

1. Replace Bits
2. [Power of Two](https://leetcode.com/problems/power-of-two/)
3. [Power of four](https://leetcode.com/problems/power-of-four/)
4. [Decode XORed Array](https://leetcode.com/problems/decode-xored-array/)
5. [Counting Bits](https://leetcode.com/problems/counting-bits/)
6. [Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)
7. [Longest Consecutive 1's](https://practice.geeksforgeeks.org/problems/longest-consecutive-1s-1587115620/1)
8. [Hamming Distance](https://leetcode.com/problems/hamming-distance/)
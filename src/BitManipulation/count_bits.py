def count_bits_hack(n):
    result = 0
    while n:
        n &= n - 1
        result += 1
    return result


print(count_bits_hack(16))

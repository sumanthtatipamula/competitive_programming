# Getting ith bit of a number


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


num, pos = 10, 2
bit_operations = BitOperations(num)
print(f"{pos} bit of a number {num} is {bit_operations.getithbit(pos)}")


bit_operations = BitOperations(15)
print(f"number after clearing {3} bit of {15} is {bit_operations.clearithbit(3)}")

bit_operations = BitOperations(9)
print(f"number after setting {2} bit of number {9} is {bit_operations.setithbit(2)}")

bit_operations = BitOperations(9)
print(
    f"number after updating {2} bit of number {9} is {bit_operations.updateith(2, 1)}"
)


bit_operations = BitOperations(15)
print(
    f"number after clearing {2} bits of number {15} is {bit_operations.clear_last_ith_bits(2)}"
)

bit_operations = BitOperations(31)
print(
    f"number after clearing bits from {1} to {3} of number {31} is {bit_operations.clear_bits_in_range(1, 3)}"
)

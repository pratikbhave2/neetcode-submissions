class Solution:
    def getSum(self, a: int, b: int) -> int:
        # We need masks to handle overflows
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            # Xor to get sum without carry
            sum_no_carry = (a ^ b) & mask

            # And + Left shift for carry
            carry = ((a &b) << 1) & mask

            # Update and b

            a, b = sum_no_carry, carry
        
        return a if a <= max_int else ~(a ^ mask)
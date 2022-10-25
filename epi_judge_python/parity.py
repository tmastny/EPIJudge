from test_framework import generic_test

# Definition: the parity of a binary word is 1 if the number
#   of 1s in the odd; otherwise 0

# O(n) for n-bit word
def parity_brute_force(x: int) -> int:
    
    num_ones = 0
    while x:
        num_ones += x & 1 
        x = x >> 1
    
    return num_ones % 2

# O(n) for n-bit word
def parity_brute_force_xor(x: int) -> int:
    
    odd_ones = 0
    while x:
        odd_ones ^= x & 1 
        x >>= 1
    
    return odd_ones

# faster O(n) solution.
#   x & (x - 1) sets the lowest 1 bit to 0.
#   So there are only `k` operations instead of `n`,
#   where `k is the number of 1 bits.
def parity_brute_force_faster(x: int) -> int:
    
    odd_ones = 0
    while x:
        # we alternate between odd ones and even ones 
        # until we run out of ones
        odd_ones ^= 1
        x &= x - 1
    
    return odd_ones

# use lookup table for 4-bit parities (0-15)
# and shift by 4-bits.
def parity_lookup(x: int) -> int:
    
    parity_lookup = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
    
    odd_ones = 0
    while x:
        odd_ones ^= parity_lookup[x & 15]
        x >>= 4
    
    return odd_ones
    
    
# O(log n) solution:
#   the parity of b_3b_2b_1b_0 equals the parity of
#   (b_3b_2) ^ (b_1b_0).
def parity(x: int) -> int:
    
    bits = [32, 16, 8, 4, 2, 1]
    
    for bit in bits:
        x ^= x >> bit
        
    return x & 1
    

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))

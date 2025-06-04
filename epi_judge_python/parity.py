from test_framework import generic_test

# Definition: the parity of a binary word is 1 if the number
#   of 1s in the odd; otherwise 0

# O(n) where n is number of bits
# O(log2 m) where m is number of digits
def parity_n(x: int) -> int:
    ones = 0
    while x:
        ones += x & 1
        x >>= 1

    return ones % 2

def parity_mod2(x: int) -> int:
    ones = 0
    while x:
        ones ^= 1 # count mod 2
        x &= x - 1

    return ones

PARITY_CACHE = [
    parity_mod2(i) for i in range(2**16)
]

def parity_cache(x: int) -> int:
    return (
        PARITY_CACHE[x & 0xffff] ^
        PARITY_CACHE[(x >> 16) & 0xffff] ^
        PARITY_CACHE[(x >> 32) & 0xffff] ^
        PARITY_CACHE[(x >> 48) & 0xffff]
    )

def parity(x: int) -> int:
    mask = 2**32 - 1
    bit32 = (x >> 32) ^ (x & mask)
    
    mask >>= 16
    bit16 = (bit32 >> 16) ^ (bit32 & mask)
    
    mask >>= 8
    bit8 = (bit16 >> 8) ^ (bit16 & mask)
    
    mask >>= 4
    bit4 = (bit8 >> 4) ^ (bit8 & mask)
    
    mask >>= 2
    bit2 = (bit4 >> 2) ^ (bit4 & mask)

    return (bit2 >> 1) ^ (bit2 & 1)

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))

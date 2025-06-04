from test_framework import generic_test


def swap_bits(x, i, j):
    if i > j:
        i, j = j, i

    diff = abs(i - j)

    bit_i = x & (1 << i)
    x &= ~bit_i
    bit_i <<= diff

    bit_j = x & (1 << j)
    x &= ~bit_j
    bit_j >>= diff

    return x | bit_i | bit_j


def swap_bits_flip(x, i, j):
    bit_i = x & (1 << i)
    bit_j = x & (1 << j)
    
    swap = (bit_i >> i) ^ (bit_j >> j)
    x ^= (swap << i) ^ (swap << j)
    
    return x


def swap_bits_book(x, i, j):
    bit_i = (x >> i) & 1 
    bit_j = (x >> j) & 1
    
    swap = bit_i ^ bit_j
    x ^= (swap << i) ^ (swap << j)
    
    return x
              


if __name__ == "__main__":
    generic_test.generic_test_main("swap_bits.py", "swap_bits.tsv", swap_bits)
    generic_test.generic_test_main("swap_bits.py", "swap_bits.tsv", swap_bits_flip)
    generic_test.generic_test_main("swap_bits.py", "swap_bits.tsv", swap_bits_book)

from test_framework import generic_test

def closet_int_same_bit_count_iterative(x: int) -> int:
    for i in range(64):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            return x ^ ((1 << i) | 1 << (i + 1))
            
    
    return -1


def closest_int_same_bit_count(x: int) -> int:
    lsb1 = x ^ (x & (x - 1))
    lsb0 = ~x ^ (~x & (~x - 1))
    
    if lsb1 > lsb0:
        swap_mask = lsb1 | (lsb1 >> 1)
    else:
        swap_mask = lsb0 | (lsb0 >> 1)
        
    return x ^ swap_mask


if __name__ == "__main__":
    generic_test.generic_test_main(
        "closest_int_same_weight.py",
        "closest_int_same_weight.tsv",
        closest_int_same_bit_count,
    )
    generic_test.generic_test_main(
        "closest_int_same_weight.py",
        "closest_int_same_weight.tsv",
        closet_int_same_bit_count_iterative,
    )


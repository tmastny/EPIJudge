from test_framework import generic_test


def reverse_bits(x: int) -> int:
    x = ((x & 0x5555_5555_5555_5555) << 1) | ((x & 0xAAAA_AAAA_AAAA_AAAA) >> 1)
    x = ((x & 0x3333_3333_3333_3333) << 2) | ((x & 0xCCCC_CCCC_CCCC_CCCC) >> 2)
    x = ((x & 0x0F0F_0F0F_0F0F_0F0F) << 4) | ((x & 0xF0F0_F0F0_F0F0_F0F0) >> 4)
    x = ((x & 0x00FF_00FF_00FF_00FF) << 8) | ((x & 0xFF00_FF00_FF00_FF00) >> 8)
    x = ((x & 0x0000_FFFF_0000_FFFF) << 16) | ((x & 0xFFFF_0000_FFFF_0000) >> 16)
    x = ((x & 0x0000_0000_FFFF_FFFF) << 32) | ((x & 0xFFFF_FFFF_0000_0000) >> 32)

    return x


def reverse_bits_16(x: int) -> int:
    x = ((x & 0x5555) << 1) | ((x & 0xAAAA) >> 1)
    x = ((x & 0x3333) << 2) | ((x & 0xCCCC) >> 2)
    x = ((x & 0x0F0F) << 4) | ((x & 0xF0F0) >> 4)
    x = ((x & 0x00FF) << 8) | ((x & 0xFF00) >> 8)
    return x


REVERSE_BITS_CACHE = [reverse_bits_16(i) for i in range(2**16)]


def reverse_bits_cache(x: int) -> int:
    return (
        REVERSE_BITS_CACHE[x & 0xFFFF] << 48
        | REVERSE_BITS_CACHE[(x >> 16) & 0xFFFF] << 32
        | REVERSE_BITS_CACHE[(x >> 32) & 0xFFFF] << 16
        | REVERSE_BITS_CACHE[(x >> 48) & 0xFFFF]
    )


if __name__ == "__main__":
    generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv", reverse_bits)
    generic_test.generic_test_main(
        "reverse_bits.py", "reverse_bits.tsv", reverse_bits_cache
    )

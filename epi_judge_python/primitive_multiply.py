from test_framework import generic_test

def add(x, y):
    sum = carry = 0
    mask = 1
    loopx, loopy = x, y
    while loopx or loopy or carry:
        bitx = x & mask
        bity = y & mask

        sum |= bitx ^ bity ^ carry

        carry = bitx & bity | bitx & carry | bity & carry

        carry <<= 1
        mask <<= 1
        loopx >>= 1
        loopy >>= 1

    return sum


def multiply(x: int, y: int) -> int:
    sum = 0
    while y:
        sum = add(sum, x if y & 1 else 0)
        y >>= 1
        x <<= 1

    return sum


if __name__ == "__main__":
    generic_test.generic_test_main(
        "primitive_multiply.py", "primitive_multiply.tsv", multiply
    )

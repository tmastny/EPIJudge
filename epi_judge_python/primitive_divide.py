from test_framework import generic_test


def divide(x: int, y: int) -> int:
    """Compute x // y"""
    if x == 0:
        return 0

    mask = 1 << (x.bit_length() - 1)

    quotient = dividend = 0
    while mask:
        bit = 1 if x & mask else 0
        dividend <<= 1
        dividend |= bit

        quotient <<= 1
        if y <= dividend:
            quotient |= 1
            dividend -= y

        mask >>= 1

    return quotient

def divide_book(x: int, y: int) -> int:
    quotient, pow = 0, 32
    while x >= y:
        while (y << pow) > x:
            pow -= 1

        quotient |= 1 << pow
        x -= (y << pow)

    return quotient


if __name__ == "__main__":
    generic_test.generic_test_main(
        "primitive_divide.py", "primitive_divide.tsv", divide
    )

    generic_test.generic_test_main(
        "primitive_divide.py", "primitive_divide.tsv", divide_book
    )

from test_framework import generic_test

import math

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True

    pow = int(math.log10(x))

    while x:
        msd = x // 10**pow
        lsd = x % 10
        if msd != lsd:
            return False

        x -= msd * 10**pow
        pow -= 2
        x //= 10

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_number_palindromic.py",
            "is_number_palindromic.tsv",
            is_palindrome_number,
        )
    )

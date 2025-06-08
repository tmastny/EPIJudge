from test_framework import generic_test


def reverse(x: int) -> int:
    positive = x >= 0
    x = abs(x)

    rev = 0
    while x:
        rev *= 10
        rev += x % 10

        x //= 10

    return rev if positive else -rev


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_digits.py", "reverse_digits.tsv", reverse
        )
    )

from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    a = max(x, y)
    b = min(x, y)

    if b == 0:
        return a

    return gcd(a - a // b * b, b)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('gcd.py', 'gcd.tsv', gcd))

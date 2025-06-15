from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return "0"
    
    negative = x < 0
    x = abs(x)
    
    s = []
    while x:
        s.append(chr(x % 10 + ord('0')))
        x //= 10

    if negative:
        s.append("-")

    s.reverse()
    return "".join(s)


def string_to_int(s: str) -> int:
    start = 0
    positive = True
    if s[0] == "+":
        start = 1
    elif s[0] == "-":
        positive = False
        start = 1

    x = 0
    for i in range(start, len(s)):
        x *= 10
        x += ord(s[i]) - ord('0')

    return x if positive else -x


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))

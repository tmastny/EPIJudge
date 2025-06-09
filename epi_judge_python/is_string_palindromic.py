from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    lo, hi = 0, len(s) - 1
    while lo <= hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
        
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))

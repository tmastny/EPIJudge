from typing import List

from test_framework import generic_test

from bisect import bisect_left


def search_first_of_k_bisect(A: List[int], k: int) -> int:
    i = bisect_left(A, k)
    
    return i if 0 <= i < len(A) and A[i] == k else -1

def search_first_of_k(A: List[int], k: int) -> int:
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if A[mid] < k:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return lo if 0 <= lo < len(A) and A[lo] == k else -1 




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))

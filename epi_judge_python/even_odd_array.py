import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from math import ceil

def even_odd_indices(A: List[int]) -> None:
    offset = 0 if len(A) % 2 == 1 else 1

    for j in range(1, ceil(len(A) / 2)):
        for i in range(j, len(A) - (j - 1) - offset, 2):
            A[i], A[i + 1] = A[i + 1], A[i]

    return


def even_odd_my_approach(A: List[int]) -> None:
    even = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[i], A[even] = A[even], A[i]
            even += 1
    
    return

# inspired by dutch flag partitioning
def even_odd(A: List[int]) -> None:
    next_even, next_odd = 0, len(A) - 1
    
    # < works here, because once they are equal it doesn't matter
    # if the current element is even or odd: it's partitioned
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    
    return





@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))

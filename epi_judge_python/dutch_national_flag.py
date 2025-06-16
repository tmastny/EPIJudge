import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    lo, hi = 0, len(A) - 1
    mid = lo
    pivot = A[pivot_index]
    while mid <= hi:
        if A[mid] == pivot:
            mid += 1
        elif A[mid] < pivot:
            A[lo], A[mid] = A[mid], A[lo]
            lo += 1
            mid += 1
        else:
            A[mid], A[hi] = A[hi], A[mid]
            hi -= 1

    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


def dutch4(A: list[int]) -> None:
    unique = set(A)
    k1, k2, k3, k4 = sorted(unique)

    i1, i2, i3, i4 = 0, 1, len(A) - 2, len(A) - 1
    for i in range(len(A)):
        if not unique:
            break
        elif k1 in unique and A[i] == k1:
            A[i], A[i1] = A[i1], A[i]
            i1 += 1
            unique.remove(k1)
        elif k2 in unique and A[i] == k2:
            A[i], A[i2] = A[i2], A[i]
            i2 += 1
            unique.remove(k2)
        elif k3 in unique and A[i] == k3:
            A[i], A[i3] = A[i3], A[i]
            i3 -= 1
            unique.remove(k3)
        elif k4 in unique and A[i] == k4:
            A[i], A[i4] = A[i4], A[i]
            i4 -= 1
            unique.remove(k4)

    while i2 <= i3:
        if A[i2] == k1:
            A[i2], A[i1] = A[i1], A[i2]
            i1 += 1
            i2 += 1
        elif A[i2] == k2:
            i2 += 1
        elif A[i2] == k3:
            A[i2], A[i3] = A[i3], A[i2]
            i3 -= 1
        elif A[i2] == k4:
            A[i2], A[i4] = A[i4], A[i2]
            A[i2], A[i3] = A[i3], A[i2]
            i3 -= 1
            i4 -= 1


def test_dutch4():
    A = [1, 1, 1, 2, 2, 1, 4, 3, 1, 3, 4]
    dutch4(A)
    print(A)

def dutch4_2(A: list[int]):
    """
    <i1 = k1
    [i1, i2) = k2
    [i2, i3] = unclassifed
    (i3, i4] = k3
    >i4 = k4
    """
    k1, k2, k3, k4 = set(A)
    i1 = i2 = 0
    i3 = i4 = len(A) - 1
    while i2 <= i3:
        if A[i2] == k1:
            A[i2], A[i1] = A[i1], A[i2]
            i1 += 1
            i2 += 1
        elif A[i2] == k2:
            i2 += 1
        elif A[i2] == k3:
            A[i2], A[i3] = A[i3], A[i2]
            i3 -= 1
        else:
            A[i2], A[i4] = A[i4], A[i2]
            i4 -= 1
            i3 -= 1

def test_dutch4_2():
    A = [1, 1, 1, 2, 2, 1, 4, 3, 1, 3, 4]
    dutch4_2(A)
    print(A)


def dutchb(A: list[tuple[bool, int]]) -> None:
    i1 = len(A) - 1
    for i in range(len(A) - 1, -1, -1):
        if A[i][0]:
            A[i], A[i1] = A[i1], A[i]
            i1 -= 1

def test_dutchb():
    A = [(bool(n), i) for i, n in enumerate([
        0, 1, 0, 0, 1, 1, 0, 1
    ])]
    dutchb(A)
    print(A)




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))

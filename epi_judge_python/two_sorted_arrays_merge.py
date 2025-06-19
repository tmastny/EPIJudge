from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    i = m + n - 1
    while m > 0 and n > 0:
        if A[m - 1] > B[n - 1]:
            A[i] = A[m - 1]
            m -= 1
        else:
            A[i] = B[n - 1]
            n -= 1
        i -= 1

    C, k = (A, m) if m > 0 else (B, n)
    while k > 0:
        A[i] = C[k - 1]
        k -= 1
        i -= 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "two_sorted_arrays_merge.py",
            "two_sorted_arrays_merge.tsv",
            merge_two_sorted_arrays_wrapper,
        )
    )

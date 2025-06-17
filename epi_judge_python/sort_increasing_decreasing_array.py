
from test_framework import generic_test

from typing import List
from operator import le, ge
import heapq

INC = 0
DEC = 1

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    if len(A) <= 3:
        return sorted(A)

    heap = []

    i = 0
    while i + 1 < len(A) and A[i] == A[i + 1]:
        i += 1

    if i + 1 == len(A):
        return A

    while i + 1 < len(A):
        start = i
        if A[i] < A[i + 1]:
            op, direction = le, INC
        else:
            op, direction = ge, DEC

        while i + 1 < len(A) and op(A[i], A[i + 1]):
            i += 1

        if direction == INC:
            heap.append((A[start], start, INC))
        else:
            heap.append((A[i], i, DEC))


    print(heap)

    B = []
    heapq.heapify(heap)
    while heap:
        val, idx, direction = heapq.heappop(heap)
        B.append(val)
        if direction == INC and idx + 1 < len(A) and A[idx] <= A[idx + 1]:
            heapq.heappush(heap, (A[idx + 1], idx + 1, INC))
        elif (
            direction == DEC and (
                idx - 1 == 0 and A[idx - 1] >= A[idx] or
                idx - 2 >= 0 and A[idx - 2] >= A[idx - 1]
            )
        ):
            heapq.heappush(heap, (A[idx - 1], idx - 1, DEC))

    return B


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))

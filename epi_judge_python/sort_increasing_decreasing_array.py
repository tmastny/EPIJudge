
from test_framework import generic_test

from typing import List
from operator import le, ge
import heapq

INC = True
DEC = False

def sort_k_increasing_decreasing_array_old(A: List[int]) -> List[int]:
    if len(A) <= 3:
        return sorted(A)

    heap = []

    dir = None
    i = 0
    while i < len(A):
        start = i
        while i + 1 < len(A) and A[i] == A[i + 1]:
            i += 1

        if dir is None:
            dir = INC if i + 1 < len(A) and A[i] < A[i + 1] else DEC

        op = le if dir == INC else ge
        while i + 1 < len(A) and op(A[i], A[i + 1]):
            i += 1

        if dir == INC:
            heap.append((A[start], start, i, INC))
        else:
            heap.append((A[i], start, i, DEC))

        dir = not dir
        i += 1


    B = []
    heapq.heapify(heap)
    while heap:
        val, start, end, dir = heapq.heappop(heap)
        B.append(val)
        if dir == INC and start < end:
            heapq.heappush(heap, (A[start + 1], start + 1, end, INC))
        elif dir == DEC and start < end:
            heapq.heappush(heap, (A[end - 1], start, end - 1, DEC))

    return B

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    heap = []
    dir = INC
    start_idx = 0
    for i in range(len(A)):
        if (
            i == len(A) - 1 or
            A[i] > A[i + 1] and dir == INC or
            A[i] <= A[i + 1] and dir == DEC
        ):
            if dir == INC:
                heap.append((A[start_idx], start_idx, i, INC))
            else:
                heap.append((A[i], start_idx, i, DEC))

            start_idx = i + 1
            dir = not dir

    B = []
    heapq.heapify(heap)
    while heap:
        val, start, end, dir = heapq.heappop(heap)
        B.append(val)
        if dir == INC and start < end:
            heapq.heappush(heap, (A[start + 1], start + 1, end, INC))
        elif dir == DEC and start < end:
            heapq.heappush(heap, (A[end - 1], start, end - 1, DEC))

    return B


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))

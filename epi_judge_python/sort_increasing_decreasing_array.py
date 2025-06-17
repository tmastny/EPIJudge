from typing import List

from test_framework import generic_test

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
    if i + 1 < len(A) and A[i] < A[i + 1]:
        heap.append((A[0], 0, INC))

    i = len(A) - 1
    while i - 1 >= 0 and A[i - 1] == A[i]:
        i -= 1
    if i - 1 >= 0 and A[i - 1] > A[i]:
        heap.append((A[len(A) - 1], len(A) - 1, DEC))

    for i in range(1, len(A) - 2):
        if A[i - 1] > A[i] < A[i + 1]:
            heap.append((A[i - 1], i - 1, DEC))
            heap.append((A[i], i, INC))

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

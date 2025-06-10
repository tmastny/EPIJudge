from typing import List

from test_framework import generic_test

import heapq

from collections import namedtuple

minArray = namedtuple('MinArray', ['min', 'idx', 'array'])

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap = [minArray(array[0], 0, array) for array in sorted_arrays]
    heapq.heapify(heap)

    merged = []
    while heap:
        min, idx, array = heapq.heappop(heap)
        merged.append(min)

        idx += 1
        if idx < len(array):
            heapq.heappush(heap, minArray(array[idx], idx, array))

    return merged


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))

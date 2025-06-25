from typing import Iterator, List

from test_framework import generic_test

import heapq
from heapq import heappop


def sort_approximately_sorted_array_old(sequence: Iterator[int], k: int) -> List[int]:
    heap = []
    output = []
    for n in sequence:
        heapq.heappush(heap, n)
        if len(heap) == k + 1:
            output.append(heapq.heappop(heap))
    
    while heap:
        output.append(heapq.heappop(heap))
           
    return output

def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    heap = []
    output = []
    
    for i, n in enumerate(sequence):
        heapq.heappush(heap, n)
        if i == k:
            break
        
    for n in sequence:
        output.append(heapq.heappushpop(heap, n))
        
    while heap:
        output.append(heapq.heappop(heap))
    
    return output

def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py",
            "sort_almost_sorted_array.tsv",
            sort_approximately_sorted_array_wrapper,
        )
    )

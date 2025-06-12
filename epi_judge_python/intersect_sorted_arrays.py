from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    merged = []
    while A and B:
        if A[-1] < B[-1]:
            B.pop()
        elif A[-1] > B[-1]:
            A.pop()
        else:
            element, _ = A.pop(), B.pop()
            if not merged or merged[-1] != element:
                merged.append(element)
        
    merged.reverse()
    return merged


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))

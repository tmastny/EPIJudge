from typing import List

from test_framework import generic_test

from math import inf

def can_reach_end_steps(A: List[int]) -> bool:
    steps = -inf
    for i, next_steps in enumerate(A):
        if i == len(A) - 1:
           return True

        steps = max(steps, next_steps)
        if steps == 0:
            break

        steps -= 1

    return False


def can_reach_end(A: List[int]) -> bool:
    idx = 0
    for i, steps in enumerate(A):
        if i > idx:
            break
        
        idx = max(idx, i + steps)
        if idx >= len(A) - 1:
            return True

    return False




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))

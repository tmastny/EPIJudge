from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value_old(A: List[int]) -> int:
    t = sum(A) + 1
    row = [0 for _ in range(t + 1)]
    row[0] = 1
    for i in range(len(A)):
        for j in range(t, A[i] - 1, -1):
            row[j] += row[j - A[i]]

    return row.index(0)

def smallest_nonconstructible_value(A: List[int]) -> int:
    A.sort()
    max_con = 0
    for a in A:
        if a > max_con + 1:
            break
        max_con += a
        
    return max_con + 1 




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))

from typing import List

from test_framework import generic_test, test_utils


def permutations_set(A: List[int]) -> List[List[int]]:
    output = []
    def bt(p, used):
        if len(p) == len(A):
            output.append(p[:])
            return

        for i in range(len(A)):
            if i not in used:
                p.append(A[i])
                used.add(i)
                bt(p, used)
                p.pop()
                used.remove(i)

    bt([], set())
    return output


def permutations_swap(A: List[int]) -> List[List[int]]:
    output = []
    def bt(idx):
        if idx == len(A):
            output.append(A[:])
            return

        for i in range(idx, len(A)):
            A[idx], A[i] = A[i], A[idx]
            bt(idx + 1)
            A[idx], A[i] = A[i], A[idx]

    bt(0)
    return output

def next_permutation(B):
    lo = (len(B) - 1) - 1
    while lo >= 0 and B[lo] > B[lo + 1]:
        lo -= 1

    if lo < 0:
        return []

    # Find the smallest number greater than lo
    min_idx = min_val = None
    for i in range(lo + 1, len(B)):
        if B[lo] < B[i] and (min_val is None or B[i] < min_val):
            min_val = B[i]
            min_idx = i
    
    B[lo], B[min_idx] = B[min_idx], B[lo]

    lo += 1
    hi = len(B) - 1
    while lo < hi:
        B[lo], B[hi] = B[hi], B[lo]
        lo += 1
        hi -= 1

    return B

def permutations(A: List[int]) -> List[List[int]]:
    A.sort()
    perms = []
    while A:
        perms.append(A.copy())
        A = next_permutation(A)

    return perms

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))

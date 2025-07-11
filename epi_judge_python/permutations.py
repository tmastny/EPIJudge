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


def permutations(A: List[int]) -> List[List[int]]:
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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))

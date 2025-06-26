from typing import List

from test_framework import generic_test


def n_queens_first(n: int) -> List[List[int]]:
    queens = []
    def find(row, positions):
        if row == n:
            if len(positions) == n:
                queens.append(positions[:])
            return

        for col in range(n):
            valid = True
            for x in range(row):
                y = positions[x]
                slope = abs((col - y) // (row - x))
                remainder = abs(col - y) % abs(row - x)
                if col == y or slope == 1 and remainder == 0:
                    valid = False
                    break

            if valid:
                positions.append(col)
                find(row + 1, positions)
                positions.pop()

    find(0, [])
    return queens


def n_queens(n: int) -> List[List[int]]:
    queens = []
    def find(row, positions):
        if row == n:
            if len(positions) == n:
                queens.append(positions[:])
            return

        for col in range(n):
            valid = True
            for x in range(row):
                y = positions[x]
                if col == y or abs(col - y) == abs(x - row): 
                    valid = False
                    break

            if valid:
                positions.append(col)
                find(row + 1, positions)
                positions.pop()

    find(0, [])
    return queens




def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))

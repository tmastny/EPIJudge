from typing import List

from test_framework import generic_test


def plus_one1(A: List[int]) -> List[int]:
    carry = 1
    for i in range(len(A) - 1, -1, -1):
       sum = A[i] + carry
       carry = sum // 10
       A[i] = sum % 10

       if not carry:
           break

    if carry:
        A.insert(0, carry)

    return A

def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        
        A[i] = 0
        A[i - 1] += 1
    
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))

from typing import List

from test_framework import generic_test

from bisect import bisect_left


def search_first_of_k_bisect(A: List[int], k: int) -> int:
    i = bisect_left(A, k)

    return i if 0 <= i < len(A) and A[i] == k else -1

def search_first_of_k(A: List[int], k: int) -> int:
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if A[mid] < k:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo if 0 <= lo < len(A) and A[lo] == k else -1

def search_greater_than_k(A: List[int], k: int) -> int:
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if A[mid] <= k:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo

def test_search_greater_than_k():
    A = [-14, -1, 2, 108, 108, 243, 285, 285, 285, 401]
    assert search_greater_than_k(A, 285) == 9

def search_local_min(A: List[int]) -> int:
    """
    Find i such that A[i - 1] >= A[i] <= A[i + 1]
    """
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if A[mid - 1] >= A[mid] <= A[mid + 1]:
            return mid
        elif A[mid - 1] < A[mid]:
            hi = mid
        else:
            lo = mid + 1

    return -1

def test_search_local_min():
    # Test case: search_local_min(A)
    # A[0] >= A[1] and A[n - 2] <= A[n - 1]
    # where len(A) = n and A is unsorted otherwise
    #
    # Find i such that A[i - 1] >= A[i] <= A[i + 1]
    # if it exists.

    # Test case 1: Simple case with local min in the middle
    A1 = [5, 3, 7, 1, 6, 8]  # A[0]=5 >= A[1]=3, A[4]=6 <= A[5]=8
    # Local min at index 3: A[2]=7 >= A[3]=1 <= A[4]=6
    result1 = search_local_min(A1)
    assert result1 == 1

    # Test case 2: Local min at index 1 (early in array)
    A2 = [10, 2, 5, 3, 7, 9]  # A[0]=10 >= A[1]=2, A[4]=7 <= A[5]=9
    # Local min at index 1: A[0]=10 >= A[1]=2 <= A[2]=5
    result2 = search_local_min(A2)
    assert result2 == 1

    # Test case 3: Multiple local minima - should return any valid one
    A3 = [8, 1, 4, 2, 6, 7]  # A[0]=8 >= A[1]=1, A[4]=6 <= A[5]=7
    # Local min at index 1: A[0]=8 >= A[1]=1 <= A[2]=4
    # Local min at index 3: A[2]=4 >= A[3]=2 <= A[4]=6
    result3 = search_local_min(A3)
    assert result3 == 1

    # Test case 4: Larger array
    A4 = [15, 10, 12, 5, 8, 3, 9, 11]  # A[0]=15 >= A[1]=10, A[6]=9 <= A[7]=11
    # Local min at index 3: A[2]=12 >= A[3]=5 <= A[4]=8
    result4 = search_local_min(A4)
    assert result4 == 3

    # Test case 5: Edge case with small array
    A5 = [6, 2, 5]  # A[0]=6 >= A[1]=2, A[1]=2 <= A[2]=5
    # Local min at index 1: A[0]=6 >= A[1]=2 <= A[2]=5
    result5 = search_local_min(A5)
    assert result5 == 1

    print("All test cases passed!")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))

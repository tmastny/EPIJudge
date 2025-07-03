from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times.sort()
    
    total_time = wait_time = 0
    for query_time in service_times:
        total_time += wait_time
        wait_time += query_time

    return total_time


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))

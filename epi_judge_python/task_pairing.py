import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    pairs = []

    task_durations.sort()
    lo, hi = 0, len(task_durations) - 1
    while lo <= hi:
        pairs.append(PairedTasks(task_durations[lo], task_durations[hi]))
        lo += 1
        hi -= 1

    return pairs


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))

from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    n = 1
    head = tail = ListNode()
    tail.next = L

    node = L
    while node and n < start:
        tail = node
        node = node.next
        n += 1

    while n < finish:
        nextnode = node.next
        node.next = nextnode.next
        nextnode.next = tail.next
        tail.next = nextnode
        n += 1

    return head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )

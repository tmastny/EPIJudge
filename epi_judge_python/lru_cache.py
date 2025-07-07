from test_framework import generic_test
from test_framework.test_failure import TestFailure


class ListNode:
    def __init__(
        self,
        key: int = -1,
        data: int = -1,
        prev: "ListNode | None" = None,
        next: "ListNode | None" = None,
    ) -> None:
        self.key = key
        self.data = data
        self.prev = prev
        self.next = next


class Lru:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.nodes = {}
        self.head = self.tail = ListNode()

    def insert(self, key, data) -> None:
        if len(self.nodes) == self.capacity:
            lru_node = self.head.next
            self.head.next = lru_node.next
            if lru_node.next:
                lru_node.next.prev = self.head
            del self.nodes[lru_node.key]

        self.tail.next = ListNode(key, data)
        self.tail = self.tail.next
        self.nodes[key] = self.tail

    def lookup(self, key) -> int:
        self.update(key)
        return self.tail.data

    def update(self, key) -> None:
        node = self.nodes[key]
        if node == self.tail:
            return

        node.prev.next = node.next
        node.next.prev = node.prev

        self.tail.next = node
        node.prev = self.tail
        node.next = None

        self.tail = node


class LruCache:
    def __init__(self, capacity: int) -> None:
        # TODO - you fill in here.
        return

    def lookup(self, isbn: int) -> int:
        # TODO - you fill in here.
        return 0

    def insert(self, isbn: int, price: int) -> None:
        # TODO - you fill in here.
        return

    def erase(self, isbn: int) -> bool:
        # TODO - you fill in here.
        return True


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))

from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import OrderedDict


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


class LruCacheListNode:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.nodes = {}
        self.head = self.tail = ListNode()

    def insert(self, key: int, data: int) -> None:
        if key in self.nodes:
            self._update(key)
            return 
            
        if len(self.nodes) == self.capacity and self.head.next:
            lru_node = self.head.next
            self._delete(lru_node.key)
            
        self.tail.next = ListNode(key, data, prev=self.tail)
        self.tail = self.tail.next
        self.nodes[key] = self.tail

    def lookup(self, key: int) -> int:
        if key not in self.nodes:
            return -1
            
        self._update(key)
        return self.tail.data

    def erase(self, key: int) -> bool:
        if key not in self.nodes:
            return False
        
        self._delete(key) 
        return True

    def _update(self, key: int) -> None:
        node = self.nodes[key]
        if node == self.tail:
            return

        node.prev.next = node.next
        node.next.prev = node.prev

        self.tail.next = node
        node.prev = self.tail
        node.next = None

        self.tail = node
    
    def _delete(self, key: int) -> None:
        self._update(key)
        del self.nodes[key]
        self.tail = self.tail.prev

class LruCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.nodes = OrderedDict()

    def insert(self, key: int, data: int) -> None:
        if key in self.nodes:
            self.nodes.move_to_end(key)
            return 
            
        if len(self.nodes) == self.capacity:
            self.nodes.popitem(False)
            
        self.nodes[key] = data 

    def lookup(self, key: int) -> int:
        if key not in self.nodes:
            return -1
            
        self.nodes.move_to_end(key)
        return self.nodes[key]

    def erase(self, key: int) -> bool:
        if key not in self.nodes:
            return False
        
        del self.nodes[key]
        return True

def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != "LruCache":
        raise RuntimeError("Expected LruCache as first command")

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == "lookup":
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    "Lookup: expected " + str(cmd[2]) + ", got " + str(result)
                )
        elif cmd[0] == "insert":
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == "erase":
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    "Erase: expected " + str(cmd[2]) + ", got " + str(result)
                )
        else:
            raise RuntimeError("Unexpected command " + cmd[0])


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lru_cache.py", "lru_cache.tsv", lru_cache_tester
        )
    )

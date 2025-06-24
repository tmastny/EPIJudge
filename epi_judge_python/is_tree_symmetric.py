from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque

def is_symmetric_bfs(tree: BinaryTreeNode | None) -> bool:
    if not tree:
        return True

    q = deque([tree])
    while q:
        next = []
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                next.append(node.left)
                next.append(node.right)

        lo, hi = 0, len(next) - 1
        while lo <= hi:
            if (
                not next[lo] and next[hi] or
                next[lo] and not next[hi] or
                next[lo] and next[hi] and next[lo].data != next[hi].data
            ): 
                return False
            
            lo += 1
            hi -= 1

        q.extend(next)

    return True

def is_symmetric(tree: BinaryTreeNode | None) -> bool:
    if not tree:
        return True
        
    def symmetric(left_tree, right_tree):
        if not left_tree and not right_tree:
            return True
        elif (
            left_tree and not right_tree or
            not left_tree and right_tree or
            left_tree.data != right_tree.data
        ):
            return False

        return (
            symmetric(left_tree.left, right_tree.right) and
            symmetric(left_tree.right, right_tree.left)
        )
        
    return symmetric(tree.left, tree.right)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))

from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    order = []
    def dfs(node):
        if not node:
            return

        order.append(node.data)
        dfs(node.left)
        dfs(node.right)

    dfs(tree)
    return order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))

from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    order = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        order.append(node.data)
    
    dfs(tree) 
    return order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))

from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    order = []
    def dfs(node):
        if not node:
            return
            
        dfs(node.left)
        order.append(node.data)
        dfs(node.right)
        
    dfs(tree)
    
    return order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))

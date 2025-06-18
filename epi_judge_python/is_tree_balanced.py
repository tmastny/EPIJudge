from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    balanced = True
    def height(node):
        if not node:
            return -1
        elif not node.left and not node.right:
            return 0

        lh = height(node.left)
        rh = height(node.right)
        if abs(lh - rh) > 1:
            nonlocal balanced
            balanced = False

        return 1 + max(lh, rh)

    height(tree)
    return balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))

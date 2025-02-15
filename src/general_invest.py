#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def find_max_at_depth(node, depth, current_depth=0):
    """Функция для нахождения максимального значения на указанной глубине."""
    if node is None:
        return float('-inf')

    if current_depth == depth:
        return node.value

    left_max = find_max_at_depth(node.left, depth, current_depth + 1)
    right_max = find_max_at_depth(node.right, depth, current_depth + 1)

    return max(left_max, right_max)


def main():
    root = BinaryTreeNode(
        3,
        BinaryTreeNode(1, BinaryTreeNode(0), None),
        BinaryTreeNode(5, BinaryTreeNode(4), BinaryTreeNode(6)),
    )

    limit = 2
    max_value = find_max_at_depth(root, limit)
    print(f"Максимальное значение на указанной глубине: {max_value}")


if __name__ == "__main__":
    main()

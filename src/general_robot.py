#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, depth_limit):
    """Функция поиска с ограничением по глубине."""
    if node is None:
        return False

    if node.value == goal:
        return True

    if depth_limit <= 0:
        return False

    return (depth_limited_search(node.left, goal, depth_limit - 1) or
            depth_limited_search(node.right, goal, depth_limit - 1))


def main():
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, None, BinaryTreeNode(4)),
        BinaryTreeNode(3, BinaryTreeNode(5), None)
    )

    goal = 4
    limit = 2

    found = depth_limited_search(root, goal, limit)
    print(f"Найден на глубине: {found}")


if __name__ == "__main__":
    main()

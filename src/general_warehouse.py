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
    """Функция поиска с ограничением по глубине для нахождения цели."""
    if node is None:
        return None

    if node.value == goal:
        return node

    if depth_limit <= 0:
        return None

    left_result = depth_limited_search(node.left, goal, depth_limit - 1)
    if left_result:
        return left_result

    return depth_limited_search(node.right, goal, depth_limit - 1)


def main():
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, None, BinaryTreeNode(4)),
        BinaryTreeNode(3, BinaryTreeNode(5), None)
    )

    goal = 4
    limit = 2

    result = depth_limited_search(root, goal, limit)
    if result:
        print(f"Цель найдена: {result}")
    else:
        print("Цель не найдена")


if __name__ == "__main__":
    main()

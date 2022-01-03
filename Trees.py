import unittest
from typing import Optional, List


class Node:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(vals: List[int]):
        """Create binary tree from list of breadth first values. Pops values from list to make nodes until final value
        is reached. Assumes that levels are fully defined, even if the maximum depth of a given position of the tree has
        already been reached.
        Example input: [1, None, 3, None, None, 4, 5]
        """

        if vals:
            root = Node(vals.pop(0))
            level = [root]
        else:
            return None

        while vals:

            next_level = []
            for el in level:
                left = vals.pop(0)
                if left:
                    el.left = Node(left)

                next_level.append(el.left)

                right = vals.pop(0)
                if right:
                    el.right = Node(right)

                next_level.append(el.right)

            level = next_level

        return root

    def to_list(self) -> List[int]:
        """Breadth first traversal of binary tree, returns list of node values"""
        # TODO: Include None values in list?

        level = [self] if self else []
        values = []

        while level:
            children = []
            for el in level:
                # Grab node value, add children to list (if present)
                values.append(el.val)
                if el.left:
                    children.append(el.left)
                if el.right:
                    children.append(el.right)

            level = children

        return values

    def insert(self, data, left=True):
        """Insert a node to the left or right of a leaf node"""
        if self.data:
            if left:
                self.left = Node(data)
            else:
                self.right = Node(data)

    def insert_ordered(self, data):
        """Insert a node in order within a binary tree (ordered left to right)"""
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


class Solution:
    def traverse_inorder(self, node):
        """Traverse tree in order (left, root, right)"""
        res = []
        if node:
            res = self.traverse_inorder(node.left)
            res.append(node.val)
            res = res + self.traverse_inorder(node.right)

        return res

    def traverse_preorder(self, node):
        """Traverse tree in order (root, left, right)"""
        res = []
        if node:
            res.append(node.val)
            res = res + self.traverse_inorder(node.left)
            res = res + self.traverse_inorder(node.right)

        return res

    def traverse_postorder(self, node):
        """Traverse tree in order (left, right, root)"""
        res = []
        if node:
            res = self.traverse_inorder(node.left)
            res = res + self.traverse_inorder(node.right)
            res.append(node.val)

        return res

    @staticmethod
    def max_depth(root: Optional[Node]) -> int:
        """Breadth first search to find maximum depth of binary tree. From root node, children are added to a new list
        that will be searched in during next loop iteration. Continues down through every level of tree"""
        depth = 0
        level = [root] if root else []

        while level:
            children = []
            depth += 1
            for el in level:
                if el.left:
                    children.append(el.left)

                if el.right:
                    children.append(el.right)

            level = children

        return depth

    @staticmethod
    def invert_tree(root: Optional[Node]) -> Optional[Node]:
        """Invert binary tree; swap left and right values, retain and return root node"""
        level = [root] if root else []

        while level:
            children = []
            for i in range(len(level)):

                if i < len(level) // 2:
                    level[i].val, level[-i-1].val = level[-i-1].val, level[i].val

                if level[i].left:
                    children.append(level[i].left)

                if level[i].right:
                    children.append(level[i].right)

            level = children

        return root


def example_tree():
    vals = [3, 9, 20, 15, 7]
    nodes = []

    for val in vals:
        nodes.append(Node(val))

    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    root.right.left = nodes[3]
    root.right.right = nodes[4]

    return root


class TestTress(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_to_list(self):
        data = [([1, 2, 3, 4, None, 6, 7], [1, 2, 3, 4, 6, 7])]

        i = 0
        for inp, out in data:
            root = Node.from_list(inp)
            with self.subTest(i=i):
                self.assertEqual(root.to_list(), out)

    def test_traverse_inorder(self):
        data = [([3, 9, 20, None, None, 15, 7], [9, 3, 15, 20, 7])]
        i = 0
        for inp, out in data:
            root = Node.from_list(inp)
            with self.subTest(i=i):
                self.assertEqual(self.solution.traverse_inorder(root), out)
            i += 1

    def test_traverse_preorder(self):
        data = [([3, 9, 20, None, None, 15, 7], [3, 9, 15, 20, 7])]
        i = 0
        for inp, out in data:
            root = Node.from_list(inp)
            with self.subTest(i=i):
                self.assertEqual(self.solution.traverse_preorder(root), out)
            i += 1

    def test_traverse_postorder(self):
        data = [([3, 9, 20, None, None, 15, 7], [9, 15, 20, 7, 3])]
        i = 0
        for inp, out in data:
            root = Node.from_list(inp)
            with self.subTest(i=i):
                self.assertEqual(self.solution.traverse_postorder(root), out)
            i += 1

    def test_max_depth(self):
        data = [([3, 9, 20, None, None, 15, 7], 3),
                ([1, None, 2], 2)]
        i = 0
        for inp, out in data:
            root = Node.from_list(inp)
            with self.subTest(i=i):
                self.assertEqual(self.solution.max_depth(root), out)
            i += 1

    def test_invert_tree(self):
        data = [([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
                ([2, 1, 3], [2, 3, 1]),
                ([], [])]
        i = 0
        for inp, out in data:
            root = Node.from_list(inp)
            res = self.solution.invert_tree(root)
            res = res.to_list() if res else []
            with self.subTest(i=i):
                self.assertEqual(res, out)
            i += 1


if __name__ == "__main__":
    unittest.main(verbosity=2)

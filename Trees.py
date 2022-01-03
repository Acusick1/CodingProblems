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
        v = vals.pop(0)
        if v:
            root = Node(v)
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

    def maxDepth(self, root: Optional[Node]) -> int:
        """Breadth first search to find maximum depth of binary tree. From root node, children are added to a new list
        that will be searched in during next loop iteration. Continues down through every level of tree"""
        depth = 0
        children = []
        level = [root] if root else []

        while level:
            depth += 1
            for el in level:
                if el.left:
                    children.append(el.left)
                elif el.right:
                    children.append(el.right)

            level = children

        return depth


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

    def test_traverse_inorder(self):
        root = Node.from_list([3, 9, 20, None, None, 15, 7])
        data = [(root, [9, 3, 15, 20, 7])]
        i = 0
        for inp, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.traverse_inorder(inp), out)
            i += 1

    def test_traverse_preorder(self):
        root = Node.from_list([3, 9, 20, None, None, 15, 7])
        data = [(root, [3, 9, 15, 20, 7])]
        i = 0
        for inp, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.traverse_preorder(inp), out)
            i += 1

    def test_traverse_postorder(self):
        root = Node.from_list([3, 9, 20, None, None, 15, 7])
        data = [(root, [9, 15, 20, 7, 3])]
        i = 0
        for inp, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.traverse_postorder(inp), out)
            i += 1


if __name__ == "__main__":

    unittest.main(verbosity=2)

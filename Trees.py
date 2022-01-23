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
        """Create binary tree from list of breadth first values. Pop values from list to make nodes until final value
        is reached. Assumes that levels are fully defined, even if the maximum depth of a given position of the tree has
        already been reached.
        Example input: [1, None, 3, None, None, 4, 5]
        """
        # TODO: pop from beginning is slow
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
        if self.val:
            if left:
                self.left = Node(data)
            else:
                self.right = Node(data)

    def insert_ordered(self, data):
        """Insert a node in order within a binary tree (ordered left to right)"""
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data


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
                    level[i].val, level[-i - 1].val = level[-i - 1].val, level[i].val

                if level[i].left:
                    children.append(level[i].left)

                if level[i].right:
                    children.append(level[i].right)

            level = children

        return root

    @staticmethod
    def invert_tree_2(root: Optional[Node]) -> Optional[Node]:
        """Invert binary tree; swap left and right values, retain and return root node"""
        stack = [root] if root else []

        while stack:
            node = stack.pop(0)
            if node:
                # If node is not None, flip it's left and right nodes, then add these nodes to the stack
                node.left, node.right = node.right, node.left
                stack += node.left, node.right

        return root

    @staticmethod
    def is_same_tree(p: Optional[Node], q: Optional[Node]) -> bool:
        """Check if two input trees are the same using BFS"""
        # Note: Became hacky trying to satisfy test cases, recursion method in subsequent function is an improvement

        if type(p) != type(q):
            return False

        tree1 = [p] if p else []
        tree2 = [q] if q else []

        while tree1 and tree2:

            children1 = []
            children2 = []
            for node1, node2 in zip(tree1, tree2):

                if type(node1) != type(node2) or node1.val != node2.val:
                    return False

                if node1.left or node2.left:
                    children1.append(node1.left)
                    children2.append(node2.left)

                if node1.right or node2.right:
                    children1.append(node1.right)
                    children2.append(node2.right)

            tree1 = children1
            tree2 = children2

        return True

    def is_same_tree_2(self, p: Optional[Node], q: Optional[Node]) -> bool:
        """Check if two input trees are the same using recursive DFS"""
        if p or q:
            if type(p) == type(q) and p.val == q.val:

                left_equal = self.is_same_tree_2(p.left, q.left)
                right_equal = self.is_same_tree_2(p.right, q.right)
                return left_equal and right_equal
            else:
                return False
        else:
            return True

    @staticmethod
    def max_sum_path_main(root):
        """Runner function for finding maximum path sum of a given tree.
        Necessary to keep track of maximum single node sums, by setting static variable within recursive
        max_sum_path function"""
        max_sum_path.solo_path = -float('inf')

        max_path = max_sum_path(root)

        return max(max_path, max_sum_path.solo_path)


def max_sum_path(root):
    """Recursive function for finding the maximum path sum of a given tree, which can start and end at any node"""
    # Base case
    if root is None:
        return 0

    left = max_sum_path(root.left)
    right = max_sum_path(root.right)

    max_path = max(max(left, right) + root.val, root.val)
    max_solo = max(max_path, root.val + left + right)
    max_sum_path.solo_path = max(max_sum_path.solo_path, max_solo)

    return max_path


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

        # TODO: Check issue with below
        # ([1, 2, None], [1, None, 2])]

        i = 0
        for inp, out in data:
            root = Node.from_list(inp)
            res = self.solution.invert_tree(root)
            res = res.to_list() if res else []
            with self.subTest(i=i):
                self.assertEqual(res, out)
            i += 1

    def test_is_same_tree(self):

        data = [([1, 2, 3], [1, 2, 3], True),
                ([1, 2, None], [1, None, 2], False),
                ([1, 2, 1], [1, 1, 2], False),
                ([], [0], False)]
        i = 0
        for t1, t2, out in data:
            t1 = Node.from_list(t1)
            t2 = Node.from_list(t2)
            with self.subTest(i=i):
                self.assertEqual(self.solution.is_same_tree(t1, t2), out)
            i += 1

    def test_is_same_tree_2(self):

        data = [([1, 2, 3], [1, 2, 3], True),
                ([1, 2, None], [1, None, 2], False),
                ([1, 2, 1], [1, 1, 2], False),
                ([], [0], False)]
        i = 0
        for t1, t2, out in data:
            t1 = Node.from_list(t1)
            t2 = Node.from_list(t2)
            with self.subTest(i=i):
                self.assertEqual(self.solution.is_same_tree_2(t1, t2), out)
            i += 1

    def test_max_sum_path_main(self):

        data = [([1, 2, 3], 6),
                ([-10, 9, 20, None, None, 15, 7], 42),
                ([-1, -2, 10, -6, None, -3, -6], 10)]

        i = 0
        for inp, out in data:
            root = Node.from_list(inp)
            with self.subTest(i=i):
                self.assertEqual(self.solution.max_sum_path_main(root), out)
            i += 1


if __name__ == "__main__":
    unittest.main(verbosity=2)

import unittest
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Inset new interval within list of intervals, merge if needed"""
        left, i = [], -1
        for i, (x, y) in enumerate(intervals):
            if y < newInterval[0]:
                # Explicitly less than new interval
                left.append([x, y])
            elif newInterval[1] < x:
                # New interval explicitly less than current
                # Therefore decrement i as right hand side must contain current
                i -= 1
                break
            else:
                # Intervals overlap, pick min and max
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)

        return left + [newInterval] + intervals[i + 1:]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge list of intervals to ensure no overlap"""
        res = []
        # Sorting intervals by starting value
        for i in sorted(intervals, key=lambda x: x[0]):

            # If current last interval is greater than start of next
            if res and res[-1][-1] >= i[0]:
                # Set last interval to max of next interval (overlap), or current value (current extends beyond next)
                res[-1][-1] = max(i[1], res[-1][-1])
            else:
                res.append(i)

        return res


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_insert(self):
        data = [([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
                ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
                ([], [5, 7], [[5, 7]]),
                ([[1, 5]], [2, 3], [[1, 5]]),
                ([[1, 5]], [6, 8], [[1, 5], [6, 8]])]

        i = 0
        for interval, new, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.insert(interval, new), out)
            i += 1

    def test_merge(self):
        data = [([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
                ([[1, 4], [4, 5]], [[1, 5]]),
                ([[1, 3], [0, 2]], [[0, 3]]),
                ([[1, 4], [2, 3]], [[1, 4]])]

        i = 0
        for interval, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.merge(interval), out)
            i += 1


if __name__ == "__main__":
    unittest.main(verbosity=2)

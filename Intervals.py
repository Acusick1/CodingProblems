import unittest
from typing import List


class Solution:
    @staticmethod
    def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """Inset new interval within list of intervals, merge if needed
        :param intervals: list of current intervals
        :param new_interval: interval to be merged
        :return: updated intervals with new_interval merged"""
        left, i = [], -1
        for i, (x, y) in enumerate(intervals):
            if y < new_interval[0]:
                # Explicitly less than new interval
                left.append([x, y])
            elif new_interval[1] < x:
                # New interval explicitly less than current
                # Therefore decrement i as right-hand side must contain current
                i -= 1
                break
            else:
                # Intervals overlap, pick min and max
                new_interval[0] = min(new_interval[0], x)
                new_interval[1] = max(new_interval[1], y)

        return left + [new_interval] + intervals[i + 1:]

    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:
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

    @staticmethod
    def erase_overlap_intervals(intervals: List[List[int]]) -> int:
        """Remove minimum number of intervals to give non-overlapping list of intervals
        :param intervals: list of increasing intervals
        :return : number of intervals removed
        Idea is to retain a current interval, see if it compares with the next. If so, one of them must be removed,
        so pick the one with the smallest end to maximise chance that the next interval will not overlap.
        """
        curr = []
        n = 0
        # Sort intervals by start
        for i in sorted(intervals, key=lambda x: x[0]):

            # If overlap (start of next < end of previous)
            if curr and i[0] < curr[1]:

                # Pick interval which has the smallest end to retain as current
                curr = min([curr, i], key=lambda x: x[1])
                # Increase counter since one must be removed
                n += 1
            else:
                curr = i

        return n


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

    def test_erase_overlap_intervals(self):
        data = [([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
                ([[1, 2], [1, 2], [1, 2]], 2),
                ([[1, 2], [2, 3]], 0),
                ([[1, 100], [20, 40], [41, 50], [51, 99]], 1),
                ([[-3035, 30075], [1937, 6906], [11834, 20971], [44578, 45600], [28565, 37578], [19621, 34415],
                  [32985, 36313], [-8144, 1080], [-15279, 21851], [-27140, -14703], [-12098, 16264], [-36057, -16287],
                  [47939, 48626], [-15129, -5773], [10508, 46685], [-35323, -26257]], 9)]

        i = 0
        for intervals, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.erase_overlap_intervals(intervals), out)
            i += 1


def overlap(i1: List[int], i2: List[int]) -> bool:
    """Check if two intervals overlap
    Note: Simple case assuming i1 and i2 are pre-sorted by start value. Here as a sanity check.
    """
    return i2[0] < i1[1]


if __name__ == "__main__":
    unittest.main(verbosity=2)

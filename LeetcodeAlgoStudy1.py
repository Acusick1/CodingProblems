import unittest
from typing import List


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Binary search for sorted integer array
        :param nums: list of integers
        :param target: integer to find
        :return: id at which integer occurs, otherwise -1
        """
        start = 0
        end = len(nums)
        mid = end // 2

        while True:

            if nums[mid] == target:
                return mid

            elif mid == start or mid == end:
                return -1

            elif target < nums[mid]:
                end = mid

            elif target > nums[mid]:
                start = mid

            mid = (start + end) // 2

    def firstBadVersion(self, n, bad):
        """Find first bad version of API, all versions bad after first failure
        :param n: length of array
        :param bad: location of first failure (API in problem)
        """
        start = 0
        end = n

        while start < end:
            mid = (start + end) // 2

            # This condition is an API in the problem
            if mid >= bad:
                end = mid
            else:
                start = mid+1

        return start

    def searchInsert(self, nums: List[int], target: int) -> int:
        """Binary search for target integer or insertion point in sorted array
        :param nums: array of sorted integers
        :param target: integer to find
        :return: index where integer lies or index where integer would lie if inserted into array
        """
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                end = mid
            else:
                start = mid + 1

        return start

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # TODO: UNDERSTAND
        answer = [0] * len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1
        return answer

    def rotate(self, nums, k):
        # TODO: UNDERSTAND
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums)-1
        reverse(nums, 0, end-k)
        reverse(nums, end-k+1, end)
        reverse(nums, 0, end)

    def moveZeroes(self, nums: List[int]) -> None:
        """Move zeroes in array to end
        :param nums: array of integers
        :return: Do not return anything, modify nums in-place instead.
        """
        offset = 1
        i = 0
        while i <= len(nums) - offset:

            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                offset += 1
            else:
                i += 1

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        """Find two numbers that add up to target number, input guarantees exactly one solution
        :param numbers: array of non decreasing integers
        :param target: target integer
        :return: list of two indices whose values add to target, in increasing order, plus one
        """
        for i in range(len(numbers)):

            want = target - numbers[i]
            # Cheating a bit since problem specifies values < abs(1000)
            numbers[i] = 10000
            if want in numbers:

                j = numbers.index(want)
                if j > i:
                    return [i+1, j+1]

            numbers[i] = target - want


class TestAlgorithms(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_search(self):

        data = [([-1, 0, 3, 5, 9, 12], 9, 4),
                ([-1, 0, 3, 5, 9, 12], 2, -1)]

        i = 0
        for nums, target, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.search(nums, target), out)
            i += 1

    def test_firstBadVersion(self):

        data = [(5, 4, 4),
                (1, 1, 1)]

        i = 0
        for n, bad, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.firstBadVersion(n, bad), out)
            i += 1

    def test_searchInsert(self):

        data = [([1, 3, 5, 6], 5, 2),
                ([1, 3, 5, 6], 2, 1),
                ([1, 3, 5, 6], 0, 0),
                ([1], 0, 0)]
        i = 0
        for nums, target, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.searchInsert(nums, target), out)
            i += 1

    def test_rotate(self):
        pass

    def test_moveZeroes(self):

        data = [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
                ([0], [0])]

        i = 0
        for nums, out in data:
            with self.subTest(i=i):
                # Run function first as operation is in-place, not returned
                self.solution.moveZeroes(nums)
                self.assertEqual(nums, out)
            i += 1

    def test_twoSum2(self):

        data = [([2, 7, 11, 15], 9, [1, 2]),
                ([2, 3, 4], 6, [1, 3]),
                ([-1, 0], -1, [1, 2])]

        i = 0
        for nums, target, out in data:
            with self.subTest(i=i):
                # Run function first as operation is in-place, not returned
                self.assertEqual(self.solution.twoSum2(nums, target), out)
            i += 1


def main():

    unittest.main()


if __name__ == "__main__":

    main()

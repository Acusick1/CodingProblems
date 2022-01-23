import unittest
from typing import List


class Solution:

    @staticmethod
    def max_profit(prices: List[int]) -> int:

        bought_at = float('inf')
        profit = 0

        for price in prices:

            if price < bought_at:
                bought_at = price

            if price > bought_at:
                profit += price - bought_at
                bought_at = price

        return profit

    @staticmethod
    def is_prime(num: int) -> bool:
        """Define whether given integer is a prime number"""
        # If number is even, not a prime number (exception is 2, which is a prime number)
        if not num % 2 and num != 2:
            return False

        # Starting from first odd number, check if there is a remainder. If not, not a prime number
        # Do this for every odd number until greater than square root of num, since combinations of factors will repeat
        # after this, and number is a prime number
        n = 3
        while n < num**0.5:
            if num % n:
                n += 2
            else:
                return False

        return True

    @staticmethod
    def find_median(arr) -> float:

        mid = len(arr) // 2
        if len(arr) % 2:
            median = arr[mid]
        elif len(arr) > 0:
            median = (arr[mid - 1] + arr[mid]) / 2
        else:
            median = []
        return median

    @staticmethod
    def iterative_binary_search(arr, num):
        """Iterative binary search
        :param arr: list of integers to be searched
        :param num: number to be searched for within arr
        :returns: id where integer lies in array, or -1 if it is not present
        """

        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end)//2
            if num > arr[mid]:
                start = mid + 1
            elif num < arr[mid]:
                end = mid - 1
            else:
                return mid

        return -1

    def recursive_binary_search(self, arr: List[int], num: int, start: int = 0, end: int = None):
        """Recursive binary search
        :param arr: list of integers to be searched
        :param num: number to be searched for within arr
        :param start: id of where to start looking for num within arr
        :param end: id of where to stop looking for num within arr
        :returns: id where integer lies in array, or -1 if it is not present
        Note: Initially thought this could be done by inputting smaller arrays on each recursive call, therefore not
        requiring start and end inputs. However, this would require proper tracking of ids, since the id 2 (for example)
        within a smaller right hand side array in the call stack will not map correctly to the overall array"""
        if end is None:
            end = len(arr) - 1

        mid = (start + end)//2

        # Base case
        if start > end:
            return -1

        elif num > arr[mid]:
            return self.recursive_binary_search(arr, num, mid+1, end)
        elif num < arr[mid]:
            return self.recursive_binary_search(arr, num, start, mid-1)
        else:
            return mid

    @staticmethod
    def binary_insert(arr: List[int], num: int):
        """Iterative binary insert into sorted array
        :param arr: sorted list of integers
        :param num: integer to insert
        """

        # Edge cases where arr in empty or num is greater than final number
        if not arr or num > arr[-1]:
            arr.append(num)
            return arr

        start = 0
        end = len(arr) - 1
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            if num > arr[mid]:
                start = mid + 1
            elif num < arr[mid]:
                end = mid - 1
            else:
                break

        arr.insert(mid, num)
        return arr


class TestMisc(unittest.TestCase):

    def setUp(self) -> None:

        self.solution = Solution()

    def test_max_profit(self):

        data = [
            ([2, 1, 2, 0, 1], 2)]

        i = 0
        for inp, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.max_profit(inp), out)

            i += 1

    def test_is_prime(self):

        data = [(10, False),
                (7, True),
                (1027, False),
                (2, True)]

        i = 0
        for inp, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.is_prime(inp), out)

            i += 1

    def test_iterative_binary_search(self):

        data = [([1, 2, 3], 2, 1),
                ([1, 2], 2, 1),
                ([1, 2, 4], 3, -1),
                ([1], 1, 0),
                ([1], 0, -1)]

        i = 0
        for arr, num, idx in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.iterative_binary_search(arr, num), idx)
            i += 1

    def test_recursive_binary_search(self):

        data = [([1, 2, 3], 2, 1),
                ([1, 2], 2, 1),
                ([1, 2, 4], 3, -1),
                ([1], 1, 0),
                ([1], 0, -1)]

        i = 0
        for arr, num, idx in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.recursive_binary_search(arr, num), idx)
            i += 1

    def test_binary_insert(self):

        data = [([1, 2, 3], 2, [1, 2, 2, 3]),
                ([1, 2], 3, [1, 2, 3]),
                ([1, 2, 3], 5, [1, 2, 3, 5]),
                ([1, 2, 4], 3, [1, 2, 3, 4]),
                ([1], 0, [0, 1]),
                ([], 0, [0]),
                ([2, 5, 6, 6, 10], 0, [0, 2, 5, 6, 6, 10])]

        i = 0
        for arr, num, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.binary_insert(arr, num), out)
            i += 1

    def test_find_median(self):

        data = [([0, 2, 5, 6, 6, 10], 5.5)]

        i = 0
        for inp, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.find_median(inp), out)
            i += 1


if __name__ == "__main__":

    unittest.main(verbosity=2)

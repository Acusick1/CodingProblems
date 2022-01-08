import unittest
import numpy as np
from typing import List
from functools import lru_cache


def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# Now we need to reverse the elements in each row i.e relecting the matrix.

def reflect(matrix):
    for i in range(len(matrix)):  # Looping through the length of the matrix i.e row in our case
        for j in range(len(
                matrix) // 2):  # This line is the heart of the code. Because here I won't be iterating through the length. We just need to interchange the element except the middle element.
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins = sorted(coins, reverse=True)

        total = 0

        for coin in coins:

            if coin <= amount:

                total = total + amount // coin

                amount = amount % coin

                if amount == 0:
                    return total

        return -1

    def lengthOfLIS(self, nums: List[int]) -> int:

        sizes = []

        for i in range(len(nums)):

            l = [nums[i]]

            for j in range(i + 1, len(nums)):

                if nums[j] > l[-1]:
                    l.append(nums[j])

            sizes.append(len(l))

        return max(sizes)

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = np.array(matrix, dtype=int)
        ones = np.ones(matrix.shape, dtype=int)
        nRows = len(matrix)

        for i in range(nRows):

            for j, num in enumerate(matrix[i]):
                if num == 0:
                    ones[:, j] = 0
                    ones[i, :] = 0

        matrix = matrix*ones

    def rotateMatrix(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        transpose(matrix)
        reflect(matrix)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        unwrapped = []
        counter = 1

        while matrix:

            if counter in [1, 3]:

                if counter == 1:
                    ele = matrix.pop(0)
                else:
                    ele = matrix.pop()
                    ele.reverse()
            else:
                if counter == 2:
                    ele = [matrix[i].pop() for i in range(len(matrix))]
                else:
                    ele = [matrix[i].pop(0) for i in range(len(matrix))]
                    ele.reverse()

            unwrapped.extend(ele)
            matrix = [x for x in matrix if x != []]

            counter += 1
            if counter > 4:
                counter = 1

        return unwrapped

    def dfs(self, board, i, j, word):

        if board[i][j] == word[0]:

            board[i][j] = ''

            if i != 0:
                up = self.dfs(board, i - 1, j, word[1:])
            else:
                up = False

            if i != len(board):
                down = self.dfs(board, i + 1, j, word[1:])
            else:
                down = False

            if j != 0:
                left = self.dfs(board, i, j - 1, word[1:])
            else:
                left = False

            if j != len(board[0]):
                right = self.dfs(board, i, j - 1, word[1:])
            else:
                right = False

            return bool(up or down or left or right)
        else:
            board[i][j] = word[0]
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:

        for letter in word:
            for i, row in enumerate(board):
                if letter in row:
                    break
                elif i == len(board)-1:
                    return False

        i = 0
        while True:
            letter = word[0]
            if letter in board[i]:

                for j, _ in enumerate(board[i]):
                    found = self.dfs(board, i, j, word)

                    if found:
                        return True

            elif i < len(board)-1:
                i += 1
            else:
                break

        return False

    def climb_stairs(self, n: int) -> int:

        if n == 1:

            return 1

        elif n == 2:

            return 2

        else:

            return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)

    def climb_stairs2(self, n):
        if n == 1:
            return 1

        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2

        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]

            # Better solution (O(n) space)
            # tmp = b
            # b = a + b
            # a = tmp

        return res[-1]


class TestDynamicProg(unittest.TestCase):

    def setUp(self) -> None:

        self.solution = Solution()

    def test_climb_stairs(self):

        data = [(2, 2),
                (3, 3)]
        i = 0
        for inp, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.climb_stairs(inp), out)
            i += 1

    def test_climb_stairs2(self):

        data = [(2, 2),
                (3, 3)]
        i = 0
        for inp, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.climb_stairs2(inp), out)
            i += 1


if __name__ == "__main__":

    a = Solution()
    # print(a.coinChange([1, 2, 5], 11))
    # print(a.lengthOfLIS([0,1,0,3,2,3]))
    # print(a.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    # print(a.rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(a.spiralOrder([[7], [9], [6]]))
    print(a.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))

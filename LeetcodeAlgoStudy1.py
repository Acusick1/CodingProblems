from typing import List


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search for sorted integer array
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
        """
        :type n: int
        :rtype: int
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
        k, end = k % len(nums), len(nums) - 1
        reverse(nums, 0, end - k)
        reverse(nums, end - k + 1, end)
        reverse(nums, 0, end)

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
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

        return nums

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):

            want = target - numbers[i]
            numbers[i] = 10000
            if want in numbers:

                j = numbers.index(want)
                if j > i:
                    return [i+1, j+1]

            numbers[i] = target - want


if __name__ == "__main__":

    a = Solution()
    # print(a.search([-1, 0, 3, 5, 9, 12], 2))
    # print(a.firstBadVersion(5, 4))
    # print(a.searchInsert([1, 3, 5, 6], 5))
    # print(a.sortedSquares([-4, -1, 0, 5, 10]))
    # print(a.rotate([1, 2, 3, 4, 5, 6], 2))
    # print(a.moveZeroes([0, 0, 1]))
    print(a.twoSum2([2, 7, 11, 15], 9))
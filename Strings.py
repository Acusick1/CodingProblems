import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

        :param s:
        :return:
        """
        # TODO: Speed up
        used = []
        max_len, i, j = 0, 0, 0

        while i < len(s):

            char = s[i]

            if char in used:
                max_len = max(max_len, len(used))
                i -= len(used) - 1
                used = []
            else:
                used.append(char)
                i += 1

        return max(max_len, len(used))

    def reverseWords(self, s: str) -> str:
        """Reverse words in a string, preserving order and whitespace
        :param s: input string
        :return: reverse word string
        """
        words = s.split(' ')
        for i, word in enumerate(words):

            words[i] = word[::-1]

        return ' '.join(words)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        :param s1:
        :param s2:
        :return:
        """
        # TODO: Speed up
        window_size = len(s1)

        i = 0
        while i + window_size <= len(s2):

            end = i + window_size
            temp = s2[i:end]
            for j, s in enumerate(s1):

                k = temp.find(s)
                if k == -1:
                    break

                else:
                    temp = temp[:k] + temp[k + 1:]

                if j == len(s1) - 1:
                    return True

            i += 1

        return False


class TestAlgorithms(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_reverseWords(self):

        data = [("okay let's go", "yako s'tel og")]
        i = 0
        for inp, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.reverseWords(inp), out)
            i += 1

    def test_lengthOfLongestSubstring(self):

        data = [("abcabcbb", 3),
                ("pwwkew", 3),
                (" ", 1),
                ("", 0),
                ("dvdf", 3)]

        i = 0
        for inp, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.lengthOfLongestSubstring(inp), out)
            i += 1

    def test_checkInclusion(self):

        data = [("adc", "dcda", True),
                ("ccc", "cbac", False),
                ("ab", "eidbaooo", True)]

        i = 0
        for s1, s2, out in data:
            with self.subTest(i=i):
                self.assertEqual(self.solution.checkInclusion(s1, s2), out)
            i += 1
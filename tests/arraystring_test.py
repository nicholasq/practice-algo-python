import unittest

import leetcode75.arraystring as arraystring
from util import time_function

asSolution = arraystring.ArrayStringSolution()


class ArrayStringTest(unittest.TestCase):

    def test_merge_strings_alternatively(self):
        test_cases = [
            ('abc', 'def', 'adbecf'),
            ('ac', 'efgh', 'aecfgh'),
            ('', '', ''),
            ('a', '', 'a'),
            ('', 'b', 'b'),
        ]
        for one, two, expected in test_cases:
            actual = time_function(asSolution.mergeAlternatively, one, two)
            self.assertEqual(expected, actual)

    def test_gcd_of_strings(self):
        test_cases = [
            ("abcabc", "abc", "abc"),
            ("abab", "ab", "ab"),
            ("leet", "code", ""),
        ]
        for one, two, expected in test_cases:
            actual = time_function(asSolution.gcdOfStrings, one, two)
            self.assertEqual(expected, actual)

    def test_kids_with_candies(self):
        test_cases = [
            ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
            ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
            ([12, 1, 12], 10, [True, False, True]),
        ]
        for one, two, expected in test_cases:
            actual = time_function(asSolution.kidsWithCandies, one, two)
            self.assertEqual(expected, actual)

    def test_can_place_flowers(self):
        test_cases = [
            ([1, 0, 0, 0, 1], 1, True),
            ([1, 0, 0, 0, 1], 2, False),
            ([0], 1, True),
            ([0], 2, False),
            ([0, 1, 0], 1, False),
            ([0, 0, 0], 1, True),
            ([0, 0, 0], 2, True),
            ([1, 0, 0, 0, 0, 1], 2, False),
            ([0, 0, 0, 0, 0, 1, 0, 0], 0, True)
        ]
        for flowerBed, toPlant, expected in test_cases:
            actual = time_function(asSolution.canPlaceFlowers, flowerBed, toPlant)
            self.assertEqual(expected, actual, f'flowerBed={flowerBed}, toPlant={toPlant}')

    def test_reverse_vowels(self):
        test_cases = [
            ("hello", "holle"),
            ("leetcode", "leotcede"),
            (" ", " "),
            ("a.", "a."),
            ("!!!", "!!!"),
        ]
        for word, expected in test_cases:
            actual = time_function(asSolution.reverseVowels, word)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

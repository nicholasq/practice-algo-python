import unittest
import time
import leetcode75.arraystring as arraystring
from util import time_function


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
            got = time_function(arraystring.merge_strings_alternatively, one, two)
            self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()

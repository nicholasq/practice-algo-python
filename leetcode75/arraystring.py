from typing import List


def greatest_common_divisor(x, y):
    if y == 0:
        return x
    return greatest_common_divisor(y, x % y)


class ArrayStringSolution:
    # https://leetcode.com/problems/merge-strings-alternately
    def mergeAlternatively(self, one: str, two: str) -> str:
        result = ""
        count = 0
        while count < len(one) or count < len(two):
            if count < len(one):
                result += one[count]
            if count < len(two):
                result += two[count]
            count += 1

        return result

    # https://leetcode.com/problems/greatest-common-divisor-of-strings
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        gcd = greatest_common_divisor(len(str1), len(str2))

        return str1[:gcd]

    # https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
    def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:
        greatest = max(candies)
        return [x + extra_candies >= greatest for x in candies]

    # https://leetcode.com/problems/can-place-flowers
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev_is_empty = True
        count = 0
        for i in range(len(flowerbed)):
            middle_plot = flowerbed[i]
            if middle_plot == 0:
                empty_left_plot = prev_is_empty or i == 0
                empty_right_plot = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                if empty_left_plot and empty_right_plot:
                    count += 1
                    prev_is_empty = False
                else:
                    prev_is_empty = True
            else:
                prev_is_empty = False
            if count >= n:
                return True
        return n == 0


    # https://leetcode.com/problems/reverse-vowels-of-a-string
    def reverseVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')
        size = len(s)
        left, right = 0, size - 1
        result = [c for c in s]
        while left < right:
            a, b = s[left], s[right]
            if a in vowels and b in vowels:
                result[left], result[right] = b, a
                left += 1
                right -= 1
            if a not in vowels:
                left += 1
            if b not in vowels:
                right -= 1
        return ''.join(result)

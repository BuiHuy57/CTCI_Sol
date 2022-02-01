""" Given two strings, write a method to decide if one is a permutation of the other. """


class Solution:
    def checkPermutation1(self, string1: str = None, string2: str = None) -> bool:
        """Solution by sorting and comparing strings. 
            Runtime: O(nlogn)

        Args:
            string1 (str): first string
            string2 (str): second string to compare to first

        Returns:
            bool: returns whether or not strings are permutations of each other
        """

        # Make sure
        if string1 is None or string2 is None:
            return False

        # If string lengths aren't the same,
        # we know they can't be permutations of each other
        if len(string1) != len(string2):
            return False

        sorted1 = sorted(string1)
        sorted2 = sorted(string2)

        if sorted1 == sorted2:
            return True
        else:
            return False

    def checkPermutations2(self, string1: str = None, string2: str = None) -> bool:
        """ Solution by using dictionaries to store characters and comparing the two
            Runtime: O(n) """

        if string1 is None or string2 is None:
            return False

        # If string lengths aren't the same,
        # we know they can't be permutations of each other
        if len(string1) != len(string2):
            return False

        dict1 = {}
        for char in string1:
            if char not in dict1:
                dict1[char] = 1

        return True

""" Implement an algorithm to determine if a string has all unique characters. 
    What if you cannot use additional data structures? """


class Solution:
    def isUnique(self, string: str = None) -> bool:
        """Solution by using dictionary to store unique characters

        Args:
            string (str): string to be analyzed

        Returns:
            bool: Value of whether or not string has unique characters
        """

        if string is None:
            return False

        unique_strings = {}

        for char in string:
            if char in unique_strings.keys():
                return False
            else:
                unique_strings[char] = 1
        return True

    def isUniqueNoDS(self, string: str) -> bool:
        for char in string:
            for char2 in range(string[1], len(string)):
                if char == char2:
                    return False
        return True

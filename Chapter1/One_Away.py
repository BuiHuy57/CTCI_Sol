""" There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
    Given two strings, write a function to check if they are one edit (or zero edits) away """


class Solution:
    def oneAway(self, string: str, editedString: str) -> bool:
        letters_og = {}
        letters_ed = {}

        for char in string:
            if char not in letters_og:
                letters_og[char] = 1
            else:
                letters_og[char] += 1

        for char in editedString:
            if char not in letters_ed:
                letters_ed[char] = 1
            else:
                letters_ed[char] += 1

        length_difference = len(editedString) - len(string)

        if abs(length_difference) > 1:
            return False

        if length_difference == 0:
            different_chars = 0
            for char in editedString:
                if char not in letters_og:
                    different_chars += 1

            if different_chars > 1:
                return False
        elif length_difference == 1:
            for char in string:
                if char not in letters_ed:
                    return False
        elif length_difference == -1:
            for char in editedString:
                if char not in letters_og:
                    return False

        return True

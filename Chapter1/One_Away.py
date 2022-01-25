""" There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
    Given two strings, write a function to check if they are one edit (or zero edits) away """

class Solution:
    def oneAway(self, string: str, editedString: str):
        length_og = len(string)
        length_edit = len(editedString)

        letters_og = {}
        letters_ed = {}

        for char in string:
            if char not in letters_og:
                letters_og[char] = 1
            else:
                letters_og[char] += 1

        

        return True

solution = Solution()
solution.oneAway("pale", "ple") # --> True
solution.oneAway("pel", "peel") # --> True
solution.oneAway("pales", "pale") # --> True
solution.oneAway("pale", "bale") # --> True
solution.oneAway("pale", "bake") # --> False
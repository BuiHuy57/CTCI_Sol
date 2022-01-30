""" Given a string, write a function to check if it is a permutation of a palindrome.
    A palindrome is a word or phrase that is the same forwards and backwards. A permutation
    is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 
    
    Example
    
    Input: Tact Coa
    Ouput: True (permutations: "taco cat", "atco cta", etc.)
    
    """

class Solution:
    def palindromePermutation(self, string:str = None) -> bool:
        if string is None:
            return False
        
        if len(string) <= 0:
            return False

        letters = {}
        true_string = string.replace(" ","").upper()

        for char in true_string:
            if char not in letters:
                letters[char] = 1
            elif char in letters:
                letters[char] += 1

        if len(true_string) % 2 == 0:
            for letter in letters:

                # If length of string is even, we need all letters to have an even amount of occurrences
                if letters[letter] % 2 != 0:
                    return False
        else: 
            odd = 0
            for letter in letters:

                # If length of string is odd, we can have exactly one letter that has an odd amount of occurrences
                if letters[letter] % 2 != 0:
                    odd += 1

            if odd > 1:
                return False

        return True
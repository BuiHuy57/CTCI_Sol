import unittest

import Is_Unique
import Check_Permutation
import One_Away
import Palindrome_Permutation
import URLify
import String_Compression

class TestCh1(unittest.TestCase):
    def test_is_unique(self):
        true_string = "abcdefg"
        solution = Is_Unique.Solution()
        actual = solution.isUnique(true_string)
        expected = True
        self.assertEqual(actual, expected)
        
        falseString = "aaaa"
        actual = solution.isUnique(falseString)
        expected = False
        self.assertEqual(actual, expected)
        
        falseString2 = "aaabbb"
        actual = solution.isUnique(falseString2)
        expected = False
        self.assertEqual(actual, expected)
        
    def test_check_perms(self):
        solution = Check_Permutation.Solution()

        strings1 = ["abcdef", "fedbca"]
        actual = solution.checkPermutation1(strings1[0], strings1[1])
        expected = True
        self.assertEqual(actual, expected)
        
        strings2 = ["ahdehf", "fedhahnvas"]
        actual = solution.checkPermutation1(strings2[0], strings2[1])
        expected = False
        self.assertEqual(actual, expected)
        
    def test_URLify(self):
        solution = URLify.Solution()
        string = "Mr John Smith     "
        true_length1 = 13
        
        actual = solution.URLify(string, true_length1)
        expected = "Mr%20John%20Smith"
        self.assertEqual(actual, expected)
        
    def test_palindrome_perms(self):
        solution = Palindrome_Permutation.Solution()
        
        true_string = "Tact Coa"
        actual = solution.palindromePermutation(true_string)
        expected = True
        self.assertEqual(actual, expected)
        
        false_string = "avfdanjin"
        actual = solution.palindromePermutation(false_string)
        expected = False
        self.assertEqual(actual, expected)
        
    def test_one_away(self):
        solution = One_Away.Solution()
        
        case1 = ["pale", "ple"]
        actual = solution.oneAway(case1[0], case1[1])
        expected = True
        self.assertEqual(actual, expected)
        
        case2 = ["pel", "peel"]
        actual = solution.oneAway(case2[0], case2[1])
        expected = True
        self.assertEqual(actual, expected)
        
        case3 = ["pales", "pale"]
        actual = solution.oneAway(case3[0], case3[1])
        expected = True
        self.assertEqual(actual, expected)
        
        case4 = ["pale", "bale"]
        actual = solution.oneAway(case4[0], case4[1])
        expected = True
        self.assertEqual(actual, expected)
        
        case5 = ["pale", "bake"]
        actual = solution.oneAway(case5[0], case5[1])
        expected = False
        self.assertEqual(actual, expected)
        
    def test_string_comp(self):
        solution = String_Compression.Solution()
        
        string1 = "aabcccccaaa"
        actual = solution.stringCompression(string1)
        expected = "a2b1c5a3"
        self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main()
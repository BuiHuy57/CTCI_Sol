import unittest

from Chapter1 import (Is_Unique, Check_Permutation, One_Away, Palindrome_Permutation, URLify, String_Compression, Rotate_Matrix)

class Test_IsUnique(unittest.TestCase):
    def setUp(self):
        self.solution = Is_Unique.Solution()
    def test_unique(self):
        true_string = "abcdefg"
        
        actual = self.solution.isUnique(true_string)
        expected = True
        self.assertEqual(actual, expected)
        
    def test_all_duplicate(self):
        falseString = "aaaa"
        
        actual = self.solution.isUnique(falseString)
        expected = False
        self.assertEqual(actual, expected)
        
    def test_two_duplicates(self):
        falseString2 = "aaabbb"
        
        actual = self.solution.isUnique(falseString2)
        expected = False
        self.assertEqual(actual, expected)
    
    def test_input(self):
        string = None
        
        actual = self.solution.isUnique(string)
        expected = False
        self.assertEqual(actual, expected)
        
class Test_CheckPerms(unittest.TestCase):
    def setUp(self):
        self.solution = Check_Permutation.Solution()
        
    def test_perms_true(self):
        strings1 = ["abcdef", "fedbca"]
        actual = self.solution.checkPermutation1(strings1[0], strings1[1])
        expected = True
        self.assertEqual(actual, expected)
        
    def test_perms_false(self):
        strings2 = ["ahdehf", "fedhahnvas"]
        actual = self.solution.checkPermutation1(strings2[0], strings2[1])
        expected = False
        self.assertEqual(actual, expected)
        
    def test_inputs(self):
        string = None
        actual = self.solution.checkPermutation1(string)
        expected = False
        self.assertEqual(actual, expected)

class Test_URLify(unittest.TestCase):
    def setUp(self):
        self.solution = URLify.Solution()
        
    def test_normal(self):
        string = "Mr John Smith     "
        true_length1 = 13
        
        actual = self.solution.URLify(string, true_length1)
        expected = "Mr%20John%20Smith"
        self.assertEqual(actual, expected)
    
    def test_input(self):
        string = None
        true_length1 = 0
        
        actual = self.solution.URLify(string, true_length1)
        expected = None
        self.assertEqual(actual, expected)
        
class Test_Palindrome_Perm(unittest.TestCase):
    def setUp(self):
        self.solution = Palindrome_Permutation.Solution()
        
    def test_palindrome_true(self):
        true_string = "Tact Coa"
        actual = self.solution.palindromePermutation(true_string)
        expected = True
        self.assertEqual(actual, expected)
        
    def test_palindrome_false(self):
        false_string = "avfdanjin"
        actual = self.solution.palindromePermutation(false_string)
        expected = False
        self.assertEqual(actual, expected)
    
    def test_input(self):
        false_string = None
        actual = self.solution.palindromePermutation(false_string)
        expected = False
        self.assertEqual(actual, expected)

class Test_OneAway(unittest.TestCase):
    def setUp(self):
        self.solution = One_Away.Solution()
        
    def test_remove(self):
        case1 = ["pale", "ple"]
        actual = self.solution.oneAway(case1[0], case1[1])
        expected = True
        self.assertEqual(actual, expected)
    
    def test_insert(self):
        case2 = ["pel", "peel"]
        actual = self.solution.oneAway(case2[0], case2[1])
        expected = True
        self.assertEqual(actual, expected)
        
    def test_remove_end(self):
        case3 = ["pales", "pale"]
        actual = self.solution.oneAway(case3[0], case3[1])
        expected = True
        self.assertEqual(actual, expected)
        
    def test_replace(self):
        case4 = ["pale", "bale"]
        actual = self.solution.oneAway(case4[0], case4[1])
        expected = True
        self.assertEqual(actual, expected)
        
    def test_fail(self):
        case5 = ["pale", "bake"]
        actual = self.solution.oneAway(case5[0], case5[1])
        expected = False
        self.assertEqual(actual, expected)
        
class Test_String_Comp(unittest.TestCase):
    def setUp(self):
        self.solution = String_Compression.Solution()
        
    def test_string_multiple(self):
        string1 = "aabcccccaaa"
        actual = self.solution.stringCompression(string1)
        expected = "a2b1c5a3"
        self.assertEqual(actual, expected)
        
    def test_string_single(self):
        string2 = "aaaaa"
        actual = self.solution.stringCompression(string2)
        expected = "a5"
        self.assertEqual(actual, expected)
    
    
class Test_Rotate_Matrix(unittest.TestCase):
    def setUp(self):
        self.solution = Rotate_Matrix.Solution()
        
    def test_rotate_matrix(self):
        matrix1 = [[]]
        
        actual = self.solution.rotate_matrix(matrix1)
        expected = [[]]
        
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()
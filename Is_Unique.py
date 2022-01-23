""" Implement an algorithm to determine if a string has all unique characters. 
    What if you cannot use additional data structures? """

class Solution:
    def isUnique(self, string: str):
        unique_strings = {}

        for char in string:
            if char in unique_strings.keys():
                return False
            else:
                unique_strings[char] = 1
        return True

    def isUniqueNoDS(self, string: str):
        for char in string:
            for char2 in range(string[1], len(string)):
                if char == char2:
                    return False
        return True

solution = Solution()

trueString = "abcdefg"
falseString = "aaaa"
falseString2 = "aaabbb"

print(solution.isUnique(trueString))
print(solution.isUnique(falseString))
print(solution.isUnique(falseString2))

print(solution.isUniqueNoDS(trueString))
print(solution.isUniqueNoDS(falseString))
print(solution.isUniqueNoDS(falseString2))
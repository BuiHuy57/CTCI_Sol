""" Given two strings, write a method to decide if one is a permutation of the other. """

class Solution:
    def checkPermutation1(self, string1: str, string2: str):
        """ Solution by sorting and comparing strings. 
            Runtime: O(nlogn) """
        if len(string1) != len(string2):
            return False

        sorted1 = sorted(string1)
        sorted2 = sorted(string2)

        if sorted1 == sorted2:
            return True
        else :
            return False

    def checkPermutations2(self, string1: str, string2: str):
        """ Solution by 
            Runtime: O() """
        return True

solution = Solution()

strings1 = ["abcdef", "fedbca"]
strings2 = ["ahdehf", "fedhahnvas"]

print(solution.checkPermutation1(strings1[0], strings1[1]))
print(solution.checkPermutation1(strings2[0], strings2[1]))
""" Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at 
    the end to hold the additional characters, and that you are given the 'true' length of the string. 
    
    EXAMPLE: 
    Input: "Mr John Smith    ", 13
    Output: "Mr%20John%20Smith" 
    
    """

class Solution:
    def URLify(self, string: str, length: int):
        """ Solution
            Runtime: O(n) assumed from join function"""

        if(len(string) <= 0):
            return None

        true_string = string[:length]
        true_string = '%20'.join(true_string.split())

        return true_string

solution = Solution()

print(solution.URLify("Mr John Smith     ", 13))
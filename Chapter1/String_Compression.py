""" Implement a method to perform basic string compression using the counts of repeated characters.
    For example, the string aabcccccaaa would become a2b1c5a3. 
    If the "compressed" string would not become smaller than the original string, your method should return the original string.
    You can assume the string has only uppercase and lowercase letters (a-z)."""
    
class Solution():
    def stringCompression(self, string: str) -> str:
        """ Solution using for loop to check for duplicates
            Runtime: O(n)

        Args:
            string (str): input string to program

        Returns:
            str: new compressed string
        """
        count = 1
        length = len(string)
        newstring = ""
        for i in range(1, length):
            if string[i] == string[i-1]:
                count += 1
            else:
                newstring = newstring + f"{string[i-1]}{count}"
                count = 1
        
        if count > 0:
            newstring = newstring + f"{string[length-1]}{count}"
            
        return newstring
""" Implement a function to check if a linked list is a palindrome. """
from data_structs import (Node, SLinkedList)


class Solution():
    def palindrome(self, linkedlist: SLinkedList) -> bool:
        """ Function that returns whether a linked list is a palindrome
            Runtime: O(n)
            Space Complexity: O(n)

        Args:
            linkedlist (SLinkedList): linked list to be checked

        Returns:
            bool: value of whether list is palindrome
        """
        if linkedlist.head is None:
            return False

        data_list = []

        ptr = linkedlist.head

        while ptr is not None:
            data_list.append(ptr.data)
            ptr = ptr.next

        for i in range(0, len(data_list)):
            if data_list[i] != data_list[len(data_list) - 1 - i]:
                return False

        return True

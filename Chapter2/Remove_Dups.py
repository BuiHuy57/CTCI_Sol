""" Write code to remove duplicates from an unsorted linked list.
    How would you solve this problem if a temporary buffer is not allowed? """
from data_structs import (Node, SLinkedList)


class Solution:
    def remove_dups(self, linkedlist: SLinkedList = None) -> SLinkedList:
        """ Program to remove duplicates from a singly linked list using dictionaries
            Runtime: O(n)
            Space Complexity: O(n)

        Args:
            linkedlist (SLinkedList, optional): Singly linked list passed into function. Defaults to None.

        Returns:
            [SLinkedList]: Single linked list containing only unique elements of linkedlist
        """
        if linkedlist.head is None:
            return None

        item_dict = {}

        ptr = linkedlist.head
        prev_ptr: Node = None
        size = linkedlist.getsize()

        while ptr is not None:
            if ptr.data not in item_dict:
                item_dict[ptr.data] = 1
                prev_ptr = ptr
            else:
                prev_ptr.next = ptr.next
                size -= 1

            ptr = ptr.next

        linkedlist.setsize(size)

        return linkedlist

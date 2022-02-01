""" Write code to remove duplicates from an unsorted linked list.
    How would you solve this problem if a temporary buffer is not allowed? """
from data_structs import (SLinkedList)


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

        while ptr is not None:
            if ptr.data not in item_dict:
                item_dict[ptr.data] = 1
            else:
                item_dict[ptr.data] += 1

            ptr = ptr.next

        size = linkedlist.getsize()
        print(size)
        for key in item_dict.keys():
            if item_dict[key] > 1:
                curr_ptr = linkedlist.head
                prev_ptr = linkedlist.head

                while curr_ptr is not None and item_dict[key] > 1:
                    if curr_ptr.data == key:
                        print("HERE")
                        prev_ptr.next = curr_ptr.next
                        tmp_ptr = curr_ptr
                        curr_ptr = curr_ptr.next
                        tmp_ptr.next = None
                        size -= 1
                        item_dict[key] -= 1
                    else:
                        prev_ptr = curr_ptr
                        curr_ptr = curr_ptr.next

        print(f"SIZE: {size}")

        linkedlist.setsize(size)

        return linkedlist

""" Implement an algorithm to find the kth to last element of a singly linked list """
from data_structs import (Node, SLinkedList)


class Solution():
    def kth_to_last(self, linkedlist: SLinkedList = None, k: int = None) -> Node:
        """Function that returns kth to last element of singly linked list

        Args:
            linkedlist (SLinkedList, optional): Singly linked list argument. Defaults to None.
            k (int, optional): Element to find from end of list. Defaults to None.

        Returns:
            Node: kth last element to be returned
        """
        length = linkedlist.getsize()
        last_index = length - k

        assert(k > 0 and length > 0 and last_index >= 0)

        ptr = linkedlist.head

        if last_index == 0:
            return ptr

        index = 0
        while index < (last_index+1):
            ptr = ptr.next
            index += 1

        kth_last = ptr

        return kth_last

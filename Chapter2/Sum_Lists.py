""" You have two numbers represented by a linked list, where each node contains a single digit.
    The digits are stored in reverse order, such that the 1s digit is at the head of the list.
    Write a function that adds the two numbers and returns the sum as a linked list."""

from data_structs import (Node, SLinkedList)


class Solution():
    def sum_lists(self, list1: SLinkedList, list2: SLinkedList) -> SLinkedList:
        """ Function that adds two linked lists and returns sum as a linked list

        Args:
            list1 (SLinkedList): singly linked list to be added
            list2 (SLinkedList): singly linked list to be added

        Returns:
            SLinkedList: singly linked list of sum of first two list arguments
        """

        assert(list1 is not None and list2 is not None)
        assert(list1.head is not None and list2.head is not None)

        ptr1 = list1.head
        ptr2 = list2.head
        sum = SLinkedList()
        tail = None
        carry = 0

        while ptr1 is not None and ptr2 is not None:
            value = (ptr1.data + ptr2.data + carry)
            carry = (value >= 10)
            value %= 10
            node = Node(value)

            if sum.head is None:
                sum.head = node
                tail = sum.head
            else:
                tail.next = node
                tail = tail.next

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if carry:
            tail.next = Node(1)
            tail = tail.next

        return sum

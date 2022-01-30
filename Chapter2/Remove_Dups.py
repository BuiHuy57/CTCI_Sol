""" Write code to remove duplicates from an unsorted linked list.
    How would you solve this problem if a temporary buffer is not allowed? """
from data_structs import (Node, SLinkedList)

class Solution:
    def remove_dups(self, linkedlist:SLinkedList = None) -> SLinkedList:
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
        
        size = len(item_dict.keys())
        for key in item_dict.keys():
            if item_dict[key] > 1:
                tmp_ptr = linkedlist.head
                while tmp_ptr.next is not None:
                    if tmp_ptr.next.data == key:
                        next_ptr = tmp_ptr.next
                        tmp_ptr.next = next_ptr.next
                        next_ptr.next = None
                    tmp_ptr = tmp_ptr.next
                    
        linkedlist.setsize(size)
        return linkedlist
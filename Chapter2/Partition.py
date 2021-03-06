""" Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
    If x is contained within the list, the values of x only need to be after the elements less than x. The partition element x can appear anywhere
    in the "right partition"l it does not need to appear between the left and right partitions. """
from data_structs import (Node, SLinkedList)


class Solution():
    def partition(self, linkedlist: SLinkedList, partition: int) -> SLinkedList:

        if linkedlist.head is None:
            return linkedlist
        
        newlist = SLinkedList([])
        ptr = linkedlist.head
        while ptr is not None:
            if ptr.data >= partition:
                newlist.insert(ptr.data)
            ptr = ptr.next
            
        ptr = linkedlist.head
        while ptr is not None:
            if ptr.data < partition:
                newlist.insert(ptr.data)
            ptr = ptr.next

        return newlist

""" Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) 
    of a singly linked list, given only access to that node."""

from data_structs import (Node)


class Solution():
    def del_mid_node(self, node: Node = None) -> None:

        assert(node is not None)

        node_ptr = node

        while node_ptr.next is not None:
            node_ptr.data = node_ptr.next.data
            node_ptr = node_ptr.next

        node_ptr = None
        return

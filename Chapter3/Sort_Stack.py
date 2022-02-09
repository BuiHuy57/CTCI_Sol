""" Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
    The stack supports the following operations: push, pop, peek, and isEmpty."""


from data_structs import Node, SLinkedList


class Sort_Stack:
    def sort_stack(self, stack: SLinkedList = None) -> SLinkedList:
        assert(
            not stack.isEmpty())
        ptr = stack.head.next
        prev_ptr: Node = stack.head

        while ptr is not None:
            if ptr.data <= stack.head.data:
                prev_ptr.next = ptr.next
                ptr.next = stack.head
                stack.head = ptr
            prev_ptr = ptr
            ptr = ptr.next

        return stack

# Generic Linked List node implementation
class Node:
    def __init__(self, datavalue=None):
        self.data = datavalue
        self.next = None

    def __eq__(self, other=None) -> bool:
        if other is None:
            return False

        if self.data == other.data:
            return True
        return False


# Singly linked list implementation
class SLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.size = 0
        if nodes is not None:
            for i in range(0, len(nodes)):
                self.insert(nodes[i])

    def getsize(self) -> int:
        return self.size

    def setsize(self, size) -> None:
        self.size = size

    def insert(self, data) -> None:
        newData = Node(data)
        if self.head is None:
            self.head = newData
        else:
            newData.next = self.head
            self.head = newData
        self.size += 1

    def pop(self) -> Node:
        item = self.head
        self.head = item.next
        item.next = None

        return item

    def peek(self) -> Node:
        return self.head

    def printlist(self) -> None:
        ptr = self.head
        while ptr is not None:
            ptr = ptr.next

    def __eq__(self, linkedlist: object) -> bool:
        if linkedlist is None:
            return False

        if self.size != linkedlist.getsize():
            return False

        ptr = self.head
        other_ptr = linkedlist.head

        while ptr is not None and other_ptr is not None:
            if ptr.data != other_ptr.data:
                return False

            ptr = ptr.next
            other_ptr = other_ptr.next

        return True

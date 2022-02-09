""" How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time"""
from data_structs import Node


class Stack_Min:
    def __init__(self, nodes=[]) -> None:
        self.top = None
        self.prev_min = None
        self.min_node = None

        for i in range(0, len(nodes)):
            self.push(nodes[i])

    def push(self, data) -> None:
        if self.top is None:
            self.top = Node(data)
            self.min_node = self.top
            self.prev_min = self.top
        else:
            newNode = Node(data)
            newNode.next = self.top
            self.top = newNode

            if self.top.data < self.min_node.data:
                self.prev_min = self.min_node
                self.min_node = self.top

    def pop(self) -> Node:
        if self.top is None:
            raise Exception("Can't pop an empty stack")

        node = self.top

        if self.min_node == self.top:
            self.top = self.top.next
            self.min_node = self.top

        return node

    def min(self) -> Node:
        if self.min_node is None:
            raise Exception("Empty stack")

        return self.min_node

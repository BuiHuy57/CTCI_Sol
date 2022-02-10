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

    def isEmpty(self) -> bool:
        return self.head is None

    def printlist(self) -> None:
        ptr = self.head
        while ptr is not None:
            print(f"DATA: {ptr.data}")
            ptr = ptr.next

    def __eq__(self, linkedlist: object) -> bool:
        if linkedlist is None:
            return False

        ptr = self.head
        other_ptr = linkedlist.head

        while ptr is not None and other_ptr is not None:
            if ptr.data != other_ptr.data:
                return False

            ptr = ptr.next
            other_ptr = other_ptr.next

        if (ptr is not None and other_ptr is None) or (ptr is None and other_ptr is not None):
            return False

        return True


# Directed graph implementation
class DGraph:
    def __init__(self, nodes: dict = None):
        if nodes is None:
            nodes = []
        self.nodes = nodes

    def getVertices(self):
        return list(self.nodes.keys())

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes[node] = []


# Tree Node implementation
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        assert(data is not None), "Data cannot be none when creating node"
        self.data = data
        self.left: TreeNode = left
        self.right: TreeNode = right

    def insert(self, data):
        assert(data is not None), "Data cannot be none when creating node"
        if data <= self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

    def printTree(self):
        if self.left is not None:
            self.left.printTree()

        print(self.data)

        if self.right is not None:
            self.right.printTree()


# Binary Search Tree Implementation
class BST:
    def __init__(self, array: list = None):
        assert(array is not None)

        self.root = TreeNode(data=array[0])

        for node in array:
            self.root.insert(node)

    def printTree(self):
        self.root.printTree()

    def __eq__(self, tree: object) -> bool:
        if self.root.data != tree.root.data:
            return False

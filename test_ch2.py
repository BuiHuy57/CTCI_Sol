from ast import Assert
import unittest

from data_structs import (Node, SLinkedList)
from Chapter2 import (Remove_Dups, Kth_To_Last, Del_Mid_Node)


class Test_Remove_Dups(unittest.TestCase):
    def setUp(self):
        self.solution = Remove_Dups.Solution()

    def test_remove_dups(self):
        linkedlist = SLinkedList([8, 7, 7, 7, 9])

        actual = self.solution.remove_dups(linkedlist)
        expected = SLinkedList([8, 7, 9])

        self.assertEqual(actual, expected)

    def test_all_dups(self):
        linkedlist = SLinkedList([7, 7, 7, 7])

        actual = self.solution.remove_dups(linkedlist)
        expected = SLinkedList([7])

        self.assertEqual(actual, expected)


class Test_Kth_Last_El(unittest.TestCase):
    def setUp(self):
        self.solution = Kth_To_Last.Solution()

    def test_kth_last_el(self):
        linkedlist = SLinkedList([9, 8, 7, 7])
        k = 3

        actual = self.solution.kth_to_last(linkedlist, k)
        expected = Node(8)

        self.assertEqual(actual, expected)

    def test_one_element(self):
        linkedlist = SLinkedList([7])
        k = 1

        actual = self.solution.kth_to_last(linkedlist, k)
        expected = Node(7)

        self.assertEqual(actual, expected)

    def test_bad_input(self):
        linkedlist = SLinkedList([9, 8, 7, 7])
        k = -7

        with self.assertRaises(AssertionError):
            out = self.solution.kth_to_last(linkedlist, k)

    def test_empty_list(self):
        linkedlist = SLinkedList([])
        k = 3

        with self.assertRaises(AssertionError):
            out = self.solution.kth_to_last(linkedlist, k)

    def test_bad_k(self):
        linkedlist = SLinkedList([9, 8, 7, 7])
        k = 9

        with self.assertRaises(AssertionError):
            out = self.solution.kth_to_last(linkedlist, k)


class Test_Del_Mid_Node(unittest.TestCase):
    def setUp(self):
        self.solution = Del_Mid_Node.Solution()

    def test_normal(self):
        linkedlist = SLinkedList(["a", "b", "c", "d", "e", "f"])

        node = linkedlist.head
        while node.data != "c":
            node = node.next

        self.solution.del_mid_node(node)
        linkedlist.setsize(linkedlist.getsize())
        expected = SLinkedList(["a", "b", "d", "e", "f"])

        self.assertEqual(linkedlist, expected)

    def test_three_el(self):
        linkedlist = SLinkedList(["a", "b", "c"])
        node = linkedlist.head
        while node.data != "b":
            node = node.next

        self.solution.del_mid_node(node)
        expected = SLinkedList(["a", "c"])

        self.assertEqual(linkedlist, expected)

    def test_one_el(self):
        linkedlist = SLinkedList(["a"])
        node = linkedlist.head

        self.solution.del_mid_node(node)
        expected = SLinkedList(["a"])

        self.assertEqual(linkedlist, expected)

    def test_empty_list(self):
        linkedlist = SLinkedList([])
        node = linkedlist.head

        with self.assertRaises(AssertionError):
            self.solution.del_mid_node(node)


if __name__ == "__main__":
    unittest.main()

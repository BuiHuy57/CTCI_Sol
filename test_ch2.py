import unittest

from data_structs import (Node, SLinkedList)
from Chapter2 import (Remove_Dups, Kth_To_Last,
                      Del_Mid_Node, Sum_Lists, Palindrome, Partition)


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

        with self.assertRaises(AssertionError):
            self.solution.del_mid_node(node)

    def test_empty_list(self):
        linkedlist = SLinkedList([])
        node = linkedlist.head

        with self.assertRaises(AssertionError):
            self.solution.del_mid_node(node)


class Test_Sum_Lists(unittest.TestCase):
    def setUp(self):
        self.solution = Sum_Lists.Solution()

    def test_normal(self):
        list1 = SLinkedList([6, 1, 7])
        list2 = SLinkedList([2, 9, 5])

        actual = self.solution.sum_lists(list1, list2)
        expected = SLinkedList([9, 1, 2])

        self.assertEqual(actual, expected)

    def test_one_digit(self):
        list1 = SLinkedList([1])
        list2 = SLinkedList([2])

        actual = self.solution.sum_lists(list1, list2)
        expected = SLinkedList([3])

        self.assertEqual(actual, expected)

    def test_empty_list(self):
        list1 = SLinkedList([6, 1, 7])
        list2 = SLinkedList([])

        with self.assertRaises(AssertionError):
            actual = self.solution.sum_lists(list1, list2)

    def test_carry_over(self):
        list1 = SLinkedList([6, 1, 7])
        list2 = SLinkedList([4, 0, 1])

        actual = self.solution.sum_lists(list1, list2)
        expected = SLinkedList([1, 0, 1, 8])

        self.assertEqual(actual, expected)


class Test_Palindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Palindrome.Solution()

    def test_normal(self):
        linkedlist = SLinkedList(["r", "a", "c", "e", "c", "a", "r"])

        actual = self.solution.palindrome(linkedlist)
        expected = True

        self.assertEqual(actual, expected)

    def test_false(self):
        linkedlist = SLinkedList(["r", "a", "c", "e"])

        actual = self.solution.palindrome(linkedlist)
        expected = False

        self.assertEqual(actual, expected)

    def test_empty(self):
        linkedlist = SLinkedList()

        actual = self.solution.palindrome(linkedlist)
        expected = False

        self.assertEqual(actual, expected)


class Test_Partition(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Partition.Solution()

    def test_normal(self):
        linkedlist = SLinkedList([1, 2, 10, 5, 8, 5, 3])
        partition = 5

        actual = self.solution.partition(linkedlist, partition)
        expected = SLinkedList([8, 5, 5, 10, 2, 1, 3])

    def test_input(self):
        linkedlist = SLinkedList([])
        partition = 0

        actual = self.solution.partition(linkedlist, partition)
        expected = SLinkedList([])

        self.assertEqual(actual, expected)

    def test_neg_numbers(self):
        # original: 2 -> -7 -> 4 -> 0 -> -5 -> 1
        # expected: -7 -> -5 -> 2 -> 4 -> 0 -> 1
        linkedlist = SLinkedList([1, -5, 0, 4, -7, 2])
        partition = -1

        actual = self.solution.partition(linkedlist, partition)
        expected = SLinkedList([1, 0, 4, 2, -5, -7])


if __name__ == "__main__":
    unittest.main()

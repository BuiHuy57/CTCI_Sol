import unittest

from data_structs import (Node, SLinkedList)
from Chapter2 import (Remove_Dups, Kth_To_Last)


class Test_Remove_Dups(unittest.TestCase):
    def setUp(self):
        self.solution = Remove_Dups.Solution()

    # def test_remove_dups(self):
    #     linkedlist = SLinkedList([8, 7, 7, 7, 9])

    #     actual = self.solution.remove_dups(linkedlist)
    #     expected = SLinkedList([8, 7, 9])

    #     self.assertEqual(actual, expected)

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


if __name__ == "__main__":
    unittest.main()
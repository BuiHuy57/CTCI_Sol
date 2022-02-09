import unittest

from data_structs import (Node, SLinkedList)
from Chapter3 import (Stack_Min, Animal_Shelter, Sort_Stack)


class Test_Stack_Min(unittest.TestCase):
    def setUp(self):
        self.stack_min = Stack_Min.Stack_Min()

    def test_funcs(self):
        self.stack_min.push(7)
        self.stack_min.push(8)
        self.stack_min.pop()

        actual = self.stack_min.min()
        expected = Node(7)

        self.assertEqual(actual, expected)

    def test_empty_pop(self):
        with self.assertRaises(Exception):
            self.stack_min.pop()

    def test_empty_min(self):
        with self.assertRaises(Exception):
            self.stack_min.min()


class Test_Animal_Shelter(unittest.TestCase):
    def setUp(self):
        self.shelter = Animal_Shelter.Animal_Shelter()

    def test_funcs(self):
        self.shelter.enqueue("Marvin", "Dog")
        self.shelter.enqueue("Sparkey", "Cat")
        self.shelter.enqueue("Bob", "Dog")
        self.shelter.enqueue("Bill", "Cat")
        self.shelter.enqueue("Jake", "Cat")

        actual = self.shelter.dequeueAny()
        expected = Node("Jake")

        self.assertEqual(actual, expected)

    def test_cats(self):
        print("test_cats")
        self.shelter.enqueue("Jake", "Cat")
        self.shelter.enqueue("Marvin", "Dog")

        actual = self.shelter.dequeueCat()
        expected = Node("Jake")

        self.assertEqual(actual, expected)

    def test_dogs(self):
        print("test_dogs")
        self.shelter.enqueue("Marvin", "Dog")
        self.shelter.enqueue("Jake", "Cat")

        actual = self.shelter.dequeueDog()
        expected = Node("Marvin")

        self.assertEqual(actual, expected)

    def test_empty_pop(self):
        with self.assertRaises(Exception):
            self.shelter.dequeueAny()

    def test_empty_cats(self):
        with self.assertRaises(Exception):
            self.shelter.dequeueCat()

    def test_empty_dogs(self):
        with self.assertRaises(Exception):
            self.shelter.dequeueDog()


class Test_Sort_Stack(unittest.TestCase):
    def setUp(self):
        self.solution = Sort_Stack.Sort_Stack()

    def test_normal(self):
        stack = SLinkedList([7, 1, 2, 5])

        actual = self.solution.sort_stack(stack)
        expected = SLinkedList([7, 5, 2, 1])

        self.assertEqual(actual, expected)

    def test_bad_input(self):
        stack = SLinkedList([])

        with self.assertRaises(Exception):
            actual = self.solution.sort_stack(stack)

    def test_neg_nums(self):
        stack = SLinkedList([-7, 1, 0, -6])

        actual = self.solution.sort_stack(stack)
        expected = SLinkedList([1, 0, -6, -7])

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

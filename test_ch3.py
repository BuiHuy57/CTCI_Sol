import unittest

from data_structs import (Node)
from Chapter3 import (Stack_Min, Animal_Shelter)


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
        
        actual = self.shelter.dequeueAny()
        expected = Node("Sparkey")
        
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


if __name__ == "__main__":
    unittest.main()
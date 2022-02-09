""" An animal shelter, which holds only dogs and cats, operates on a strictly "First in, first out" basis.
    People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
    They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
    You may use the built-in LinkedList data structure """

from data_structs import Node, SLinkedList


class Animal_Shelter():
    def __init__(self) -> None:
        self.shelter = SLinkedList([])
        self.dogs = SLinkedList([])
        self.cats = SLinkedList([])

    def enqueue(self, name: str = "", type: str = "") -> None:
        self.shelter.insert(name)
        if type.lower() == "dog":
            self.dogs.insert(name)
        elif type.lower() == "cat":
            self.cats.insert(name)

    def dequeueAny(self) -> Node:
        if self.shelter.head is None:
            raise Exception("Can't dequeue empty stack")

        animal = self.shelter.pop()
        if animal.data == self.dogs.peek().data:
            self.dogs.pop()
        elif animal.data == self.cats.peek().data:
            self.cats.pop()

        return animal

    def dequeueDog(self) -> Node:
        if self.dogs.head is None:
            raise Exception("Can't dequeue empty stack")

        animal = self.dogs.pop()
        ptr = self.shelter.head
        prev_ptr: Node = None

        while ptr is not None:
            if ptr.data == animal.data:
                prev_ptr.next = ptr.next
                ptr = prev_ptr
            else:
                prev_ptr = ptr
                ptr = ptr.next

        return animal

    def dequeueCat(self) -> Node:
        if self.cats.head is None:
            raise Exception("Can't dequeue empty stack")

        animal = self.cats.pop()
        ptr = self.shelter.head
        prev_ptr: Node = None

        while ptr is not None:
            if ptr.data == animal.data:
                prev_ptr.next = ptr.next
                ptr = prev_ptr
            else:
                prev_ptr = ptr
                ptr = ptr.next

        return animal

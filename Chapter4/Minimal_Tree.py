""" Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height. """

from data_structs import (BST)


class MinimalTree:
    def minimalTree(self, array: list = None):
        assert(array is not None)
        return BST(array)

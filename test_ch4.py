import unittest

from data_structs import (BST, DGraph)
from Chapter4 import (Route_Btwn_Nodes, Minimal_Tree)


class Test_Route_Btwn_Nodes(unittest.TestCase):
    def setUp(self):
        self.solution = Route_Btwn_Nodes.Route_Btwn_Nodes()

    def test_true_route(self):
        graph = DGraph({
            "a": ["b", "c"],
            "b": ["a", "d"],
            "c": ["a", "d"],
            "d": ["e"],
            "e": ["d"]
        })
        node1 = "a"
        node2 = "b"

        actual = self.solution.route_between_nodes(graph, node1, node2)
        expected = True
        self.assertEqual(actual, expected)

    def test_false_route(self):
        graph = DGraph({
            "a": ["b", "c"],
            "b": ["a", "d"],
            "c": ["a", "d"],
            "d": ["e"],
            "e": ["d"]
        })
        node1 = "a"
        node2 = "d"

        actual = self.solution.route_between_nodes(graph, node1, node2)
        expected = False
        self.assertEqual(actual, expected)

    def test_bad_graphs(self):
        graph = None

        with self.assertRaises(AssertionError):
            actual = self.solution.route_between_nodes(graph, "a", "b")

    def test_bad_nodes(self):
        graph = DGraph({
            "a": ["b", "c"],
            "b": ["a", "d"],
            "c": ["a", "d"],
            "d": ["e"],
            "e": ["d"]
        })
        node1 = "a"
        node2 = None

        with self.assertRaises(AssertionError):
            actual = self.solution.route_between_nodes(graph, node1, node2)

    def test_empty_graph(self):
        graph = DGraph()

        actual = self.solution.route_between_nodes(graph, "a", "b")
        expected = False
        self.assertEqual(actual, expected)


class Test_Minimal_Tree(unittest.TestCase):
    def setUp(self):
        self.solution = Minimal_Tree.MinimalTree()

    def test_normal(self):
        array = [1, 2, 3, 4, 5]

        actual = self.solution.minimalTree(array)
        expected = BST([1, 2, 3, 4, 5])

        self.assertEqual(actual, expected)

    def test_no_array(self):
        array = None

        with self.assertRaises(AssertionError):
            actual = self.solution.minimalTree(array)


if __name__ == "__main__":
    unittest.main()

import unittest

from data_structs import (Graph_Node, DGraph)
from Chapter4 import (Route_Btwn_Nodes)


class Test_Route_Btwn_Nodes(unittest.TestCase):
    def setUp(self):
        self.solution = Route_Btwn_Nodes.Route_Btwn_Nodes()

    def test_funcs(self):

        actual = self.solution.route_between_nodes()
        expected = Node(7)

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

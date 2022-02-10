""" Given a directed graph, design an algorithm to find out whether there is a route between two nodes. """


from data_structs import DGraph


class Route_Btwn_Nodes:
    def route_between_nodes(self, graph: DGraph = None, node1=None, node2=None):
        assert(graph is not None and node1 is not None and node2 is not None)

        if not node1 in graph.nodes or not node2 in graph.nodes:
            return False

        if node2 not in graph.nodes[node1]:
            return False
        elif node2 in graph.nodes[node1]:
            return True

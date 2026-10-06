from aiden.agent.graph.edge import Edge
from aiden.agent.graph.node import Node

class Graph:

    def __init__(self) -> None:
        self.nodes : dict[str,Node] = {} #{[Str, Node]}
        self.edges : list[Edge] = []

    def add_node(self,node : Node)-> None :
        self.nodes[node.name] = node

    def add_edge(self,edge : Edge) -> None :
        self.edges.append(edge)

    def get_node(self, name : str) -> Node :
        if name not in self.nodes :
            raise KeyError(f"Node not found: {name}")
        return self.nodes[name]

    def get_edge(self, source : str)-> list[Edge] :
        return [
            edge for edge in self.edges
            if edge.source == source
        ]
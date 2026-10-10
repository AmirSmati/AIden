from aiden.agent.graph.edge import Edge
from aiden.agent.graph.node import Node
from aiden.agent.graph.gate import DecisionGate

class Graph:

    def __init__(self) -> None:
        self.nodes : dict[str,Node] = {} #{[Str, Node]}
        self.edges : list[Edge] = []
        self.gates : dict[str , DecisionGate] = {}

    def add_node(self,node : Node)-> None :
        self.nodes[node.name] = node

    def add_edge(self,edge : Edge) -> None :
        self.edges.append(edge)

    def get_node(self, name : str) -> Node :
        if name not in self.nodes :
            raise KeyError(f"Node not found: {name}")
        return self.nodes[name]

    def get_edges(self, source : str | None = None)-> list[Edge] :
        if not source :
            return []
        return [
            edge for edge in self.edges
            if edge.source == source
        ]

    def add_gate(self, source : str, dec_gate : DecisionGate) -> None : 
        if source not in self.nodes : 
            raise KeyError(f"Node not found: {source}")
        self.gates[source] = dec_gate

    def get_gate(self,source:str) -> DecisionGate | None : 
        return self.gates.get(source)
import networkx as nx
from typing import Dict
from typing import List
from node import Node
from transmission import Transmission
class Graph:
    def __init__(self, ):
        self.__nodes : Dict[str, Node] = {}
        self.__transmissions : List[Transmission] = []
        self.__graph = nx.Graph()

    def add_node(self, node: Node):
        self.__nodes[node.node_id] = node
        self.__graph.add_node(node.node_id, obj = node)

    def add_transmission(self, transmission: Transmission):
        self.__transmissions.append(transmission)

        # To denote the start and end points
        start_id = transmission.get_transmission()[0].node_id
        end_id = transmission.get_transmission()[1].node_id

        # To create the edge of the graph
        self.__graph.add_edge(start_id, end_id, obj = transmission,
                              capacity = transmission.get_capacity(),
                              resistance = transmission.get_resistance())

    def node_validity(self, node : Node):
        if node.node_id in self.__nodes:
            return True
        else:
            return False

    def connected_nodes (self, node: Node):
        return list(self.__graph.neighbors(node.node_id))

    def get_all_generators(self):
        generator_list = []
        for node in self.__nodes.values():
            if node.get_info()["Type"] == "generator":
                generator_list.append(node)
        return generator_list

    def get_all_consumers(self):
        consumer_list = []
        for node in self.__nodes.values():
            if node.get_info()["Type"] == "consumer":
              consumer_list.append(node)

        return consumer_list




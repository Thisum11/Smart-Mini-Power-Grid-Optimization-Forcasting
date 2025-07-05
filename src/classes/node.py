from dataclasses import dataclass

@dataclass
class Node:
    nodeID : str
    name : str
    node_type : str
    connections = []

    # validating the data class
    def __post_init__(self):
        valid_types = {"generator", "consumer", "junction"}
        if self.node_type.lower() not in valid_types:
            raise ValueError(f"Invalid node type: {self.node_type}")

    # Returning the information
    def get_info(self):
        return {
            "ID"   : self.nodeID,
            "Name" : self.name,
            "Type" : self.node_type,
        }

    # allowing nodes to create
    def connection(self, other):
        self.connections.append(other)

    def get_connections(self):
        return self.connections


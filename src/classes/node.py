from dataclasses import dataclass

@dataclass
class Node:
    nodeID : str
    name : str
    node_type : str

    # validating the data class
    def __post_init__(self):
        valid_types = {"generator", "consumer", "junction"}
        if self.node_type.lower() not in valid_types:
            raise ValueError(f"Invalid node type: {self.node_type}")


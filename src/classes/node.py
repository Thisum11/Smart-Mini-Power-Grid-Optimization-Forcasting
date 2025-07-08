from typing import Tuple
class Node:
    def __init__(self, node_id: str, name:str, node_type:str, region:str, location: Tuple[float, float] = (0,0)):

        # validating the data
        valid_types = {"generator", "consumer", "junction"}
        if self.__node_type.lower() not in valid_types:
            raise ValueError(f"Invalid node type: {self.__node_type}")

        self.__node_id = node_id
        self.__name = name
        self.__node_type = node_type.lower()
        self.__region = region
        self.__location = location
        self.__connections = []

    # Returning the information
    def get_info(self):
        return {
            "ID"   : self.__node_id,
            "Name" : self.__name,
            "Type" : self.__node_type,
        }

    # allowing nodes to create
    def connection(self, other):
        self.__connections.append(other)

    def get_connections(self):
        return self.__connections

    @property
    def node_id(self):
        return self.__node_id

    def get_node_type(self):
        return self.__node_type


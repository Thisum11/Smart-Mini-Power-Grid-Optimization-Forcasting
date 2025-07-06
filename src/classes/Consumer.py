from typing import Tuple
from typing import List
from node import Node

class Consumer(Node):
    def __init__(self, node_id:str, name:str, node_type:str, region:str, location: Tuple[float, float],
                 demand:List[float], consumer_type:str):
        super().__init__(node_id, name, node_type, region, location)

        self.__demand = demand
        self.__received_power = 0.0
        self.__consumer_type = consumer_type

    def get_demand(self, timestep:int) -> float:
        if 0 <= timestep < len(self.__demand):
            return self.__demand[timestep]
        else:
            raise IndexError("Timestep out of range")

    # To add the received amount
    def receive_power(self, amount:float):
        self.__received_power = amount

    # To find the unmet demand
    def unmet_demand(self, timestep:int) -> float:
        return max(0.0,self.get_demand(timestep)- self.__received_power)

    # Resets the received power to 0
    def reset(self):
        self.__received_power = 0




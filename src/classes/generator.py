from dataclasses import dataclass, field

@dataclass
class Generator:
    __name: str
    __max_capacity: float
    __min_capacity: float
    __cost: float
    __source_type: str
    __is_renewable: bool
    __current_output: float = field(default=0)

    #Generates the power amount that generates by the generator
    def generate (self, amount: float):
        if (amount <= self.__max_capacity and amount >= self.__min_capacity):
           self.__current_output = amount
        else:
            raise ValueError(f"Requested amount {amount} is out of bounds.")

    #Getter method for the cost
    @property
    def get_cost(self):
        return self.__cost

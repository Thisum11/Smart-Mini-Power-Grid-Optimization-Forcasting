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

    #Getter method for the current energy output
    @property
    def get_current_output(self):
        return self.__current_output

    #Getter method for the maximum energy output
    @property
    def get_max_capacity(self):
        return self.__max_capacity

    #Getter method for the minimum energy output
    @property
    def get_min_capacity(self):
        return self.__min_capacity

    #how much more the generation can produce
    def available_capacity(self):
        return self.__max_capacity - self.__current_output

    #the cost for the total energy production
    def generation_cost(self):
        return self.__current_output * self.__cost

    #resets the current output to 0
    def reset_output(self):
        self.__current_output = 0

    #adjusts the cost to the given value
    def adjust_cost(self, value: float):
        self.__cost = value

    def __str__(self):
        return (f"{self.__name}\n"
                f"output: {self.__current_output}\n"
                f"cost: {self.__cost}/ MWh\n"
                f" type: {self.__source_type}\n"
                f"{'Renewable' if self.__is_renewable else 'Not Renewable'}\n"
                )



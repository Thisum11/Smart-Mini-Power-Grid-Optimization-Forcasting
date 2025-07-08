class Transmission:
    def __init__(self, transmission_id : str, start : Node, end : Node, capacity : float,
                 resistance : float, length : float, current_flow: float,loss : float):

        self.__transmission_id = transmission_id
        self.__start = start
        self.__end = end
        self.__capacity = capacity
        self.__resistance = resistance
        self.__length = length
        self.__current_flow = current_flow
        self.__loss = loss
        self.__k_voltage : float = 330

    #To calculate the power loss during the transmission
    def loss_calculation (self):
        voltage : float = self.__k_voltage * 1000
        self.__loss = ((self.__current_flow**2)*self.__resistance)/(voltage**2)
        return self.__loss

    # To make sure the transmission is possible
    def transmission_status(self):
        if self.__current_flow < self.__capacity:
            return True
        else:
            return False

    # To display the transmission line
    def get_transmission(self):
        return [self.__start, self.__end]

    # To find the transmission efficiency
    def efficiency(self):
        if self.__current_flow == 0:
            efficiency = 0
        else:
            efficiency = (self.__current_flow - self.__loss) * 100 / self.__current_flow
        return efficiency

    def __str__(self):
        return (f"transmissionID: {self.__transmission_id}\n" +
                f"start: {self.__start}\n" +
                f"end: {self.__end}\n" +
                f"capacity: {self.__capacity}\n" +
                f"resistance: {self.__resistance}\n" +
                f"length: {self.__length}\n" +
                f"current flow: {self.__current_flow}\n" +
                f"loss: {self.__loss}\n" +
                f"efficiency: {self.efficiency()}")


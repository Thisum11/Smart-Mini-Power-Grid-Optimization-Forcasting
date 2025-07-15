import numpy as np
from typing import List, Tuple

from classes.generator import Generator
from classes.consumer import Consumer
from classes.transmission import Transmission
from classes.node import Node

def generator_bounds(generators: List[Generator]) -> List[Tuple[float, float]]:
    return [(gen.get_min_capacity(), gen.get_max_capacity()) for gen in generators]


def power_balance (
        generators: List[Generator],
        consumers: List[Consumer],
        timestep : int
) -> Tuple[np.ndarray, float]:
    left_eq = np.array([1.0]*len(generators))
    right_eq = sum(consumer.get_demand(timestep) for consumer in consumers)
    return left_eq, right_eq
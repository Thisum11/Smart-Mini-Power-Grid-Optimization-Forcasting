import numpy as np
from typing import List, Tuple

from classes.generator import Generator
from classes.consumer import Consumer
from classes.transmission import Transmission
from classes.node import Node

def generator_bounds(generators: List[Generator]) -> List[Tuple[float, float]]:
    for gen in generators:
        return [(gen.get_min_capacity()), (gen.get_max_capacity())]


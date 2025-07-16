import numpy as np
from typing import List, Tuple

from classes.generator import Generator
from classes.consumer import Consumer
from optimizer.constraints import (
    generator_bounds,
    power_balance
)

def build_lp_inputs(
        generators: List[Generator],
        consumers: List[Consumer],
        timestep : int
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, List[Tuple[float, float]]]:

    # Objective function --> To minimize the total generation cost
   c = np.array([gen.get_cost() for gen in generators])

   # Power balance constraints
   a_eq_row = b_eq_value = power_balance(generators, consumers, timestep)
   a_eq = np.array([a_eq_row])
   b_eq = np.array([b_eq_value])

   #Generator output bounds
   bounds = generator_bounds(generators)

   return c , a_eq, b_eq, bounds


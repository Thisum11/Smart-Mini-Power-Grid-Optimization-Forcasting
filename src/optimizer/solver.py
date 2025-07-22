import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from typing import List, Dict, Union
from scipy.optimize import linprog
from classes.generator import Generator
from classes.consumer import Consumer
from optimizer.formulations import build_lp_inputs


def run_optimization(generators: List[Generator],
                     consumers: List[Consumer],
                     timestep: int) -> Dict[str, Union[str, float, List[float]]]:

    # Build linear programming inputs
    c, a_eq, b_eq, bounds = build_lp_inputs(generators, consumers, timestep)

    # Solve using scipy.optimize.linprog
    result = linprog(c, A_eq=a_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if result.success:
        return {
            'status': 'Optimal',
            'generator_dispatch': result.x.tolist(),
            'total_cost': result.fun
        }
    else:
        return {
            'status': 'Failed',
            'message': result.message
        }

"""Repeat the following paper for `SPSOL`:
    Shi, Y. and Eberhart, R., 1998, May.
    A modified particle swarm optimizer.
    In IEEE World Congress on Computational Intelligence (pp. 69-73). IEEE.
    https://ieeexplore.ieee.org/abstract/document/699146

    Kennedy, J. and Eberhart, R., 1995, November.
    Particle swarm optimization.
    In Proceedings of International Conference on Neural Networks (pp. 1942-1948). IEEE.
    https://ieeexplore.ieee.org/document/488968

    Luckily our Python code could repeat the data generated by the other Python code *well*.
    Therefore, we argue that its repeatability could be **well-documented**.



    You can run the following Python script (note that first install `pymoo` via `pip install pymoo`):
    --------------------------------------------------------------------------------------------------
    from pymoo.algorithms.soo.nonconvex.pso import PSO
    from pymoo.problems.single import Ackley
    from pymoo.optimize import minimize

    problem = Ackley(n_var=100)
    algorithm = PSO(pop_size=20)
    res = minimize(problem=problem, algorithm=algorithm, termination=('n_eval', 1e6),  verbose=True, seed=1)
    print("Best-so-far solution found: F = %s" % (res.F))  # F = [0.19331169]
"""
import time

import numpy as np

from pypop7.benchmarks.base_functions import ackley
from pypop7.optimizers.pso.spsol import SPSOL as Solver


if __name__ == '__main__':
    start_run = time.time()
    ndim_problem = 100
    for f in [ackley]:
        print('*' * 7 + ' ' + f.__name__ + ' ' + '*' * 7)
        problem = {'fitness_function': f,
                   'ndim_problem': ndim_problem,
                   'lower_boundary': -32.768*np.ones((ndim_problem,)),
                   'upper_boundary': 32.768*np.ones((ndim_problem,))}
        options = {'max_function_evaluations': 1e6,
                   'seed_rng': 1,
                   'verbose': 1e3}
        solver = Solver(problem, options)
        results = solver.optimize()
        print(results)      # 1.745270594710746e-13 vs 0.19331169 (from pymoo)
        print('*** Runtime: {:7.5e}'.format(time.time() - start_run))

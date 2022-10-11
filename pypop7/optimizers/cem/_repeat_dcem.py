"""Repeat the following paper for `DCEM`:
    Amos, B. and Yarats, D., 2020, November.
    The differentiable cross-entropy method.
    In International Conference on Machine Learning (pp. 291-302). PMLR.
    http://proceedings.mlr.press/v119/amos20a.html

    Luckily our code could repeat the data generated by the original Python code *well*.
    Therefore, we argue that the repeatability of `DCEM` could be **well-documented**.



    You can run the following Python script (note that first download the library from
    https://github.com/facebookresearch/dcem):

    import numpy as np
    import torch

    from dcem import dcem


    def f(x):
        w = np.power(10, 6 * np.linspace(0, 1, x.shape[2]))
        x = x.detach().numpy()
        y = np.empty((1, x.shape[1]))
        for i in range(x.shape[1]):
            y[0, i] = np.dot(w, np.power(x[0, i], 2))
        y = torch.from_numpy(y)
        return y


    mu = np.random.default_rng(0).uniform(-5*np.ones((1, 100)), 5*np.ones((1, 100)))
    opt = dcem(f=f, nx=100, init_mu=torch.from_numpy(mu), init_sigma=1.0,
               n_sample=1000, n_elite=200, n_iter=int(2e6/1000), temp=1.0, iter_eps=0)
    print(f(opt.unsqueeze(1)))
"""
import time

import numpy as np

from pypop7.benchmarks.base_functions import ellipsoid
from pypop7.optimizers.cem.dcem import DCEM as Solver


if __name__ == '__main__':
    start_run = time.time()
    ndim_problem = 100
    problem = {'fitness_function': ellipsoid,
               'ndim_problem': ndim_problem,
               'lower_boundary': -5*np.ones((ndim_problem,)),
               'upper_boundary': 5*np.ones((ndim_problem,))}
    options = {'max_function_evaluations': 2e6,
               'seed_rng': 0,
               'sigma': 1.0,
               'verbose': 20,
               'saving_fitness': 2000}
    solver = Solver(problem, options)
    results = solver.optimize()
    print(ellipsoid(results['mean']))  # 3.568760205550662e-08 vs 3.6024e-08 (from the original paper)
    print('*** Runtime: {:7.5e}'.format(time.time() - start_run))

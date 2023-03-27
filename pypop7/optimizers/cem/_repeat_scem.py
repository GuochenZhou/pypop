"""Repeat the following paper for `SCEM`:
    Kroese, D.P., Porotsky, S. and Rubinstein, R.Y., 2006.
    The cross-entropy method for continuous multi-extremal optimization.
    Methodology and Computing in Applied Probability, 8(3), pp.383-407.
    https://link.springer.com/article/10.1007/s11009-006-9753-0
    (See [Appendix B Main CE Program] for the official Matlab code.)

    Luckily our Python code could repeat the data generated by the original Matlab code *well*.
    Therefore, we argue that its repeatability could be **well-documented**.



    You can run the following Matlab script (note that save function `Rosen` as a separate file):
    ---------------------------------------------------------------------------------------------
    function out = Rosen(X)
    r=[];
    for i = 1:size(X,2)-1
    r = [100*(X(:,i+1)-X(:,i).^2).^2+(X(:,i)-1).^2,r];
    end
    out = sum(r,2);
    end

    n=1000;
    N = 1000;
    Nel = 200;
    alpha = 0.8;
    mu = 2*ones(1,n);
    sigma = 10*ones(1,n);
    mu_last = mu;
    sigma_last = sigma;
    S_best_overall = Inf;
    t = 0;
    while t < 1001
    t = t + 1;
    mu = alpha*mu + (1-alpha)*mu_last;
    sigma= alpha*sigma + (1-alpha)*sigma_last;
    X = ones(N,1)*mu + randn(N,n)*diag(sigma);
    SA = Rosen(X);
    [S_sort,I_sort] = sort(SA);
    S_best = S_sort(1);
    if (S_best < S_best_overall)
    S_best_overall = S_best;
    end
    mu_last = mu;
    sigma_last = sigma;
    Xel = X(I_sort(1:Nel),:);
    mu = mean(Xel);
    sigma = std(Xel);
    end
    fprintf('%9.8f\n', S_best_overall);
"""
import time

import numpy as np

from pypop7.benchmarks.base_functions import rosenbrock
from pypop7.optimizers.cem.scem import SCEM


if __name__ == '__main__':
    start_run = time.time()
    ndim_problem = 1000
    problem = {'fitness_function': rosenbrock,
               'ndim_problem': ndim_problem,
               'lower_boundary': -5*np.ones((ndim_problem,)),
               'upper_boundary': 5*np.ones((ndim_problem,))}
    options = {'max_function_evaluations': 1000*1000,
               'mean': 2.0*np.ones((ndim_problem,)),
               'seed_rng': 0,
               'sigma': 10.0,
               'verbose': 200,
               'saving_fitness': 50000}
    scem = SCEM(problem, options)
    results = scem.optimize()
    print(results)  # 1044.879869712122 vs 1050.51959312 (from the Matlab code)
    print('*** Runtime: {:7.5e}'.format(time.time() - start_run))

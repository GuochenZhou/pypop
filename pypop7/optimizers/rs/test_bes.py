def test_optimize():
    import numpy  # engine for numerical computing
    from pypop7.benchmarks.base_functions import rosenbrock  # function to be minimized
    from pypop7.optimizers.rs.bes import BES
    problem = {'fitness_function': rosenbrock,  # to define problem arguments
               'ndim_problem': 2,
               'lower_boundary': -5.0 * numpy.ones((2,)),
               'upper_boundary': 5.0 * numpy.ones((2,))}
    options = {'max_function_evaluations': 5000,  # to set optimizer options
               'seed_rng': 2022,
               'temperature': 100.0,
               'mean': 3.0 * numpy.ones((2,))}
    bes = BES(problem, options)  # to initialize the black-box optimizer class
    results = bes.optimize()  # to run its optimization/evolution process
    assert results['n_function_evaluations'] == 5000
    assert results['best_so_far_y'] < 1.0

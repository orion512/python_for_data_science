""" List Comprehension Example 4

This module implements a vectorised equivalent
to example 1 with numpy.

Author: Dominik Zulovec Sajovic, April 2022
"""

import time
import numpy as np
from example_1 import comp_loop


all_iterations = [
    100000000,
    200000000,
]

improvements = []

for num_iterations in all_iterations:

    # Run and Time the Comprehension for loop
    start_time = time.time()
    numbers = comp_loop(num_iterations)
    elapsed_time_comp = round(time.time() - start_time, 2)

    # Run and Time the Vectorised implementation
    start_time = time.time()
    numbers = np.mod(((np.arange(num_iterations) * 4) - 7), 3) 
    elapsed_time_vec = round(time.time() - start_time, 2)

    # Analysis of the time
    if (elapsed_time_vec == 0) & (elapsed_time_comp == 0):
        times_better = 0
    else:
        times_better = round(((elapsed_time_comp - elapsed_time_vec) / elapsed_time_comp) * 100, 2)

    status = 'better' if times_better >= 0 else 'worse' 

    print(f'Over the iteration of {num_iterations:,} the vectorised implementation performed {times_better}% {status}')
    print(f'Comprehension Loop Time: {elapsed_time_comp}s')
    print(f'Vectorised implementation: {elapsed_time_vec}s')

    improvements.append(times_better)

# Plot the timing test
import matplotlib.pyplot as plt
fig = plt.figure()
all_iterations_str = [str(n) for n in all_iterations]
plt.bar(all_iterations_str, improvements)
plt.show()
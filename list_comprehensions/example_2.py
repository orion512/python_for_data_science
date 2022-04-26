""" List Comprehension Example 2

This module runs the speed test with multiple number of
iterations and compares them visually.

Author: Dominik Zulovec Sajovic, April 2022
"""

import time
from example_1 import normal_loop, comp_loop


all_iterations = [
    1000000,
    5000000,
    10000000,
    50000000,
    100000000,
    # 200000000,
    # 300000000,
    # 400000000,
    # 500000000,
    # 600000000,
    # 700000000,
    # 800000000,
    # 900000000,
    # 1000000000,
]

improvements = []

for num_iterations in all_iterations:

    # Run and Time the Comprehension for loop
    start_time = time.time()
    numbers = comp_loop(num_iterations)
    elapsed_time_comp = round(time.time() - start_time, 2)

    # Run and Time the Normal for loop
    start_time = time.time()
    numbers = normal_loop(num_iterations)
    elapsed_time_norm = round(time.time() - start_time, 2)

    # Analysis of the time
    if (elapsed_time_comp == 0) & (elapsed_time_norm == 0):
        times_better = 0
    else:
        times_better = round(((elapsed_time_norm - elapsed_time_comp) / elapsed_time_norm) * 100, 2)

    status = 'better' if times_better >= 0 else 'worse' 

    print(f'Over the iteration of {num_iterations:,} the comprehension loop performed {times_better}% {status}')
    print(f'Comprehension Loop Time: {elapsed_time_comp}s')
    print(f'Normal Loop Time: {elapsed_time_norm}s')

    improvements.append(times_better)

# Plot the timing test
import matplotlib.pyplot as plt
fig = plt.figure()
all_iterations_str = [str(n) for n in all_iterations]
plt.bar(all_iterations_str, improvements)
plt.show()
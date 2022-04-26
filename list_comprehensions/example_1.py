""" List Comprehension Example 1

This module defines two versions of for loops and performs a simple speed test

Author: Dominik Zulovec Sajovic, April 2022
"""


import time


def run_calculation(n: int):
    """ Magic happens to the passes variable n """
    return ((n*4) - 7) % 3


def normal_loop(num_iterations: int):
    """
        Looping passed number of times, performing a calculation 
        and saving the result, implemented by an oridnary for loop
    """
    numbers = []
    for i in range(num_iterations):
        numbers.append(run_calculation(i))
    return numbers


def comp_loop(num_iterations: int):
    """
        Looping passed number of times, performing a calculation 
        and saving the result, implemented with list comprehension
    """
    return [run_calculation(i) for i in range(num_iterations)]


if __name__ == "__main__":

    num_iterations = 100000000

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

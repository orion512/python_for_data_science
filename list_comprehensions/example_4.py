""" List Comprehension Example 3

This module first generates random strings.
And then uses 3 different approaches to search for substrings.
- normal for loop
- list comprehension
- list comprehension with python built-in filter

it is important to note that the preparation (generating the strings)
takes the longest.

Author: Dominik Zulovec Sajovic, April 2022
"""

import time
import random
import string

SUB_STR = 'dom'

def gen_rand_string(len: int):
    """ Generaates a random string of the specified length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len))


def contains_str(s: str):
    """ returns True if the global defined substring is 
    contained in the passed string else False """
    return True if SUB_STR in s else False


if __name__ == "__main__":
    # define number of iterations
    num_iterations = 10000000

    # generate random strings
    rand_strings = [gen_rand_string(7) for i in range(num_iterations)]

    # Look for substrings with a normal for loop
    start_time = time.time()
    mathced_strings_norm = set()
    for s in rand_strings:
        if contains_str(s):
            mathced_strings_norm.add(s)
    elapsed_time_norm = round(time.time() - start_time, 2)
    
    # Look for substrings with a list comprehension
    start_time = time.time()
    mathced_strings_comp = {s for s in rand_strings if contains_str(s)}
    elapsed_time_comp = round(time.time() - start_time, 2)

    # Look for substrings with a list comprehension
    start_time = time.time()
    mathced_strings_fil = set(filter(contains_str, rand_strings))
    elapsed_time_fil = round(time.time() - start_time, 2)

    # this line makes sure all 3 approaches work the same
    assert(mathced_strings_norm == mathced_strings_comp == mathced_strings_fil)

    print('Normal Loop: ', elapsed_time_norm, 'seconds')
    print('List Comprehension 1: ', elapsed_time_comp, 'seconds')
    print('List Comprehension 2: ', elapsed_time_fil, 'seconds')

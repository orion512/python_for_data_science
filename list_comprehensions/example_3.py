""" List Comprehension Example 3

This module ...

Author: Dominik Zulovec Sajovic, April 2022
"""

import random
import string

def gen_rand_string(len: int):
    """ Generaates a random string of the specified length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len))


def contains_str(s: str):
    return True if SUB_STR in s else False


rand_strings = [gen_rand_string(7) for i in range(10000)]

SUB_STR = 'dom'

mathced_strings = []
for s in rand_strings:
    if SUB_STR in s:
        mathced_strings.append(s)

print(mathced_strings)
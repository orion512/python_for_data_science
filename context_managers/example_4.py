""" Context Managers Example 4

This module is an example of using a context manager to read from a database.

A pre-requirement is a postgres database.

Author: Dominik Zulovec Sajovic, March 2022
"""

import contextlib


@contextlib.contextmanager
def db_handler():
    """
        This function can be transfored into a simple 
        context manager by using a contextlib decorator.
    """
    try:
        print('This is like the enter method')
        yield
    finally:
        print('This is like the exit method')


class dbhandler_decorator(contextlib.ContextDecorator):
    """
        This class can be used as a decorator.
        It can make things much simpler but unfortunatelly the
        function which uses it cannot access the returned object.
    """

    def __enter__(self):
        """ This function gets invoked at the start of a with statement """
        print('This is like the enter method')
        return 5
    
    def __exit__(self, exc_type, ex_value, ex_traceback):
        """ This function gets invoked at the end of the with statement """
        print('This is like the exit method')


@dbhandler_decorator()
def simple_fun():
    """ A simple function to test our own conext manager decorator """
    print('I am in the simple function')


# TODO: Suppress warnings



if __name__ == "__main__":
    with db_handler():
        print('This is where I do stuff')

    simple_fun()

    with dbhandler_decorator() as obj:
        print('Another way of using the decorator context manager ' + str(obj))

    # Context manager can also be used to suppress warnings where we know it is safe to ignore them
    # It is somewhat similar to running try/except block and passing an exception
    # but using supress makes it more explicit that those warnings are controlled within the logic
    # below is bad example of using suppress but it should get the point across
    with contextlib.suppress(ZeroDivisionError):
        b = 9 / 0

""" Context Managers Example 2

This module is an example of how context manager work.

Author: Dominik Zulovec Sajovic, March 2022
"""


class WalterWhiteHandler:
    """
    The Walter White Handler is a context manager 
    to help replace all the Michael Jordans
    """

    def __init__(self):
        """ initialization function for the class """
        self.f = None

    def __enter__(self):
        """ This function gets invoked at the start of a with statement """
        self.f = open("datasets/nba_scoring_champions.csv", "r")
        return self.f

    def __exit__(self, exc_type, ex_value, ex_traceback):
        """ This function gets invoked at the end of the with statement """
        print(exc_type, ex_value, ex_traceback)
        self.f.close()


def read_file_cm():
    """ This function uses the WW Handler to read the file """

    with WalterWhiteHandler() as f:
        file_content = f.read()
        print(file_content)

        replaced_content = file_content.replace('Michael Jordan', 'Walter White')
        print(replaced_content)



if __name__ == "__main__":
    read_file_cm()

""" Context Managers Example 1

This module is an example of reading a file with
and without using context managers. 

Author: Dominik Zulovec Sajovic, March 2022
"""


def read_file():
    """ This functions reads a file without using context managers """

    # open the file
    f = open("datasets/nba_scoring_champions.csv", "r")

    # do something with the file content
    file_content = f.read()
    print(file_content)

    replaced_content = file_content.replace('Michael Jordan', 'Walter White')
    print(replaced_content)

    # close the file
    f.close()


def read_file_with():
    """ This functions reads a file with using context managers """

    # with is a keyword we can use to enter and exit the context manager
    with open("datasets/nba_scoring_champions.csv", "r") as f:
        file_content = f.read()
        print(file_content)

        replaced_content = file_content.replace('Michael Jordan', 'Walter White')
        print(replaced_content)


if __name__ == "__main__":
    read_file()
    read_file_with()

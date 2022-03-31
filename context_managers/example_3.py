""" Context Managers Example 3

This module is an example of using a context manager to read from a database.

A pre-requirement is a postgres database.

Author: Dominik Zulovec Sajovic, March 2022
"""


import psycopg2
import psycopg2.extras


class DBHandler():
    """
        This class simulates a context manager wrapper
        wrapper for a postgres DB. It doesn't show any best 
        practice of how you should implement DB connections,
        it is only used to explain the function of the context
        managers.
    """

    def __init__(self, host, user, passw, db):
        """ initialization function for the class """
        self.host = host
        self.user = user
        self.passw = passw
        self.db = db
        self.conn = None
        self.cur = None

    def __enter__(self):
        """ This function gets invoked at the start of a with statement """
        self.conn = psycopg2.connect(
            dbname=self.db,
            user=self.user,
            password=self.passw,
            host=self.host,
        )
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        return self.cur

    def __exit__(self, exc_type, ex_value, ex_traceback):
        """ This function gets invoked at the end of the with statement """
        self.cur.close()
        self.conn.close()


def select_from_db():
    """ This function uses the custom made context manager to handle a db connection """
    with DBHandler('localhost', 'postgres', 'password', 'nba') as cur:
        sql_stmt = ("SELECT COUNT(id) FROM nba.game")

        cur.execute(sql_stmt)
        res = cur.fetchall()

    print(res)


def select_from_db_2():
    """ This function uses the context manager built in psycopg2 library """
    with psycopg2.connect(
        host='localhost',
        user='postgres',
        password='password',
        dbname='nba') as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            sql_stmt = ("SELECT COUNT(id) FROM nba.game")

            cur.execute(sql_stmt)
            res = cur.fetchall()

    print(res)


if __name__ == "__main__":
    select_from_db()
    select_from_db_2()

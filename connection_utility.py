import pymysql

"""
CSCI-620 - Project
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)
        Shivani Singh(ss5243@rit.edu)
        Meenu Gigi(mg2578@rit.edu)

This is a python file for MySQL connection.
"""

HOST_NAME = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""
CURRENT_DB = "playground"


def get_connection():
    """
    Establish a connection with MySQL.
    :return: MySQL connection
    """

    conn = pymysql.connect(host=HOST_NAME, port=PORT, user=USER, passwd='', db=CURRENT_DB)
    return conn


def close_connection(conn=None):
    """
    Method to close an existing connection
    :return: None
    """

    if conn:
        conn.close()

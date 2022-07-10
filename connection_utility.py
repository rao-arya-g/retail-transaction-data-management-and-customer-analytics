import pymysql

HOST_NAME = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""
CURRENT_DB = "playground"


def get_connection():
    """

    :return:
    """
    conn = pymysql.connect(host=HOST_NAME, port=PORT, user=USER, passwd='', db=CURRENT_DB)
    return conn


def close_connection(conn=None):
    """
    Method to close the existing connection
    :return:
    """
    if conn:
        conn.close()

    return None

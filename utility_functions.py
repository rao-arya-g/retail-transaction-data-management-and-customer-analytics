import pandas as pd


def load_data_from_csv(table_config):

    file_name = table_config.get('file_name')
    skiprows = table_config.get('skiprows')
    skipfooter = table_config.get('skipfooter')
    sheet_name = table_config.get('sheet_name', 0)
    data_df = create_dataframe_from_excel(file_name, skiprows, skipfooter, sheet_name)
    formatting_function = table_config.get("format_function", None)
    if callable(formatting_function):
        data_df = formatting_function(data_df)

    return data_df


def create_dataframe_from_excel(filename, skiprows=0, skipfooter=0, sheet_name=0):
    """Function to read data from csv to DataFrame"""

    try:
        data_df = pd.read_excel(filename, sheet_name=sheet_name, skiprows=skiprows, skipfooter=skipfooter)
        return data_df
    except FileNotFoundError as e:
        raise Exception("File not found. Please make sure file location is updated correctly.Error details" + str(e))


def load_data_from_mysql(sql_query, conn):
    """
    Function to load the data from the MySQL.
    :param sql_query: The SQL query corresponding the requested data
    :param conn: MySQL connection.
    :return: Pandas DataFrame corresponding to the Table data in MySQL
    """

    data_df = pd.read_sql_query(sql_query, conn)
    return data_df

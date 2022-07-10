import pandas as pd

from constants import FILE_BASED_CONFIG, MYSQL_BASED_CONFIG


def load_data_from_mysql(sql_query, conn):
    """
    Function to load the data from the MySQL.
    :param sql_query: The SQL query corresponding the requested data
    :param conn: MySQL connection.
    :return: Pandas DataFrame corresponding to the Table data in MySQL
    """

    data_df = pd.read_sql_query(sql_query, conn)
    return data_df


def create_dataframe_from_csv(filename, skiprows=0, skipfooter=0):
    """Function to read data from csv to DataFrame"""

    try:
        data_df = pd.read_excel(filename, skiprows=skiprows, skipfooter=skipfooter)
        return data_df
    except FileNotFoundError as e:
        raise Exception("File not found. Please make sure file location is updated correctly.Error details" + str(e))


def load_data_from_csv(table_config):

    file_name = table_config.get('file_name')
    skiprows = table_config.get('skiprows')
    skipfooter = table_config.get('skipfooter')
    data_df = create_dataframe_from_csv(file_name, skiprows, skipfooter)
    formatting_function = table_config.get("format_function", None)
    if callable(formatting_function):
        data_df = formatting_function(data_df)

    return data_df


def load_online_retail_data(read_from_csv=False):
    """
    Function to load the online retail data
    :param read_from_csv: Boolean flag to indicate whether reading should be done from csv or from MySQL.
    :return: Dictionary with Table Name and Corresponding data in DataFrame format.
    """

    data_df_dictionary = {}

    if read_from_csv:
        for table_name in FILE_BASED_CONFIG:
            current_config = FILE_BASED_CONFIG.get(table_name)
            data_df = load_data_from_csv(current_config)
            data_df_dictionary[table_name] = data_df
    else:
        for table_name in MYSQL_BASED_CONFIG:
            current_config = MYSQL_BASED_CONFIG.get(table_name)
            data_df = load_data_from_mysql(current_config, None)
            data_df_dictionary[table_name] = data_df
    return data_df_dictionary


def main():
    """
    Main method - Present now to test few things
    :return: None
    """
    print("Hello")


if __name__ == '__main__':
    main()

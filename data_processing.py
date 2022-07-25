from connection_utility import get_connection
from constants import FILE_BASED_CONFIG, MYSQL_BASED_CONFIG
from utility_functions import load_data_from_csv, load_data_from_mysql


def clean_online_retail_data(data_df):
    """
    Function to clean the online retail data.
    :param data_df: Online retail data
    :return: Processed data of the type DataFrame
    """

    # Remove the Entries with any records with Quantity <=0
    data_df = data_df[data_df["QUANTITY"] > 0].reset_index(drop=True)

    # Remove the Entries with Stock code as -

    data_df = data_df[~data_df["STOCK_CODE"].isin(['BANK_CHARGE'])]

    # Calculate actual price of the transaction
    data_df["PURCHASE_COST"] = data_df["QUANTITY"] * data_df["PRICE"]
    return data_df


def load_online_retail_data(read_from_csv=True):
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
        conn = get_connection()
        for table_name in MYSQL_BASED_CONFIG:
            current_config = MYSQL_BASED_CONFIG.get(table_name)
            data_df = load_data_from_mysql(current_config, conn)
            data_df_dictionary[table_name] = data_df
    return data_df_dictionary

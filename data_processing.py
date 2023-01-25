from connection_utility import get_connection
from constants import FILE_BASED_CONFIG, MYSQL_BASED_CONFIG
from utility_functions import load_data_from_excel, load_data_from_mysql

"""
Author: Arya Girisha Rao(ar1422@rit.edu)

This is a python file for Data processing.
"""


def clean_online_retail_data(data_df):
    """
    Function to clean the online retail data. Filter the data as per requirement.
    The filtering conditions are -
        1. Quantity greater than 0.
        2. Stock code is not in Bank charge.
        3. Invoice entry is not cancelled.
        4. Price of the product is greater than 1.
        5. Unique transactions.
    :param data_df: Online retail data
    :return: Processed data of the type DataFrame
    """

    data_df = data_df[data_df["QUANTITY"] > 0].reset_index(drop=True)
    data_df = data_df[~data_df["STOCK_CODE"].isin(['BANK_CHARGE'])]
    data_df["PURCHASE_COST"] = data_df["QUANTITY"] * data_df["PRICE"]
    data_df = data_df[~data_df['INVOICE_NUMBER'].astype(str).str.contains('C')]
    data_df.drop_duplicates(inplace=True)
    data_df = data_df.dropna(subset=['CUSTOMER_ID'])
    data_df = data_df[(data_df['PRICE'] > 0) & (data_df['QUANTITY'] > 0)]
    return data_df


def load_online_retail_data(read_from_csv=True):
    """
    Function to load the online retail data.
    :param read_from_csv: Boolean flag to indicate whether reading should be done from csv or from MySQL.
    :return: Dictionary with Table Name and Corresponding data in DataFrame format.
    """

    data_df_dictionary = {}

    if read_from_csv:
        for table_name in FILE_BASED_CONFIG:
            current_config = FILE_BASED_CONFIG.get(table_name)
            data_df = load_data_from_excel(current_config)
            data_df_dictionary[table_name] = data_df
    else:
        conn = get_connection()
        for table_name in MYSQL_BASED_CONFIG:
            current_config = MYSQL_BASED_CONFIG.get(table_name)
            data_df = load_data_from_mysql(current_config, conn)
            data_df_dictionary[table_name] = data_df
    return data_df_dictionary

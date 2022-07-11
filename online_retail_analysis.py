import datetime
from constants import FILE_BASED_CONFIG, MYSQL_BASED_CONFIG
from utility_functions import load_data_from_csv, load_data_from_mysql
from connection_utility import get_connection


def visualize_recency_matrix(data_df):
    """
    Function to visualize the recency matrix
    :param data_df: DataFrame of the Customers with recent buy matrix information.
    :return: None
    """
    return None


def derive_recency_matrix(data_df, reference_date=None):
    """
    Function to derive recency matrix
    :param data_df:
    :param reference_date:
    :return:
    """

    if reference_date is not None and isinstance(reference_date, str):
        reference_date = datetime.datetime.strptime(reference_date, "%m/%d/%Y").date()
    else:
        reference_date = datetime.datetime.now().date()

    data_df["INVOICE_DATE_ONLY"] = data_df["INVOICE_DATE"].apply(lambda x: x.date())
    filtered_data_df = data_df[["CUSTOMER_ID", "INVOICE_DATE_ONLY"]]
    filtered_data_df = filtered_data_df.groupby(by=["CUSTOMER_ID"]).max().reset_index()
    filtered_data_df['RECENT_DAYS_DIFF'] = filtered_data_df['INVOICE_DATE_ONLY'].apply(lambda x: (reference_date - x).days)
    return filtered_data_df


def clean_online_retail_data(data_df):
    """
    Function to clean the online retail data.
    :param data_df: Online retail data
    :return: Processed data of the type DataFrame
    """

    # Remove the Entries with any records with Quantity <=0
    data_df = data_df[data_df["QUANTITY"] < 0].reset_index(drop=True)

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


def main():
    """
    Main method - Present now to test few things
    :return: None
    """

    data_df_dictionary = load_online_retail_data()
    complete_df = clean_online_retail_data(data_df_dictionary.get("complete_retail_data"))
    derive_recency_matrix(complete_df, "01/01/2011")


if __name__ == '__main__':
    main()

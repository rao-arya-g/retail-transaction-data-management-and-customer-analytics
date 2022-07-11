import datetime

from constants import FILE_BASED_CONFIG, MYSQL_BASED_CONFIG
from utility_functions import load_data_from_csv, load_data_from_mysql
from connection_utility import get_connection
from online_retail_visualization import visualize_recency_matrix


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
    filtered_data_df['RECENCY'] = filtered_data_df['INVOICE_DATE_ONLY'].apply(lambda x: (reference_date - x).days)
    filtered_data_df = filtered_data_df[["CUSTOMER_ID", "RECENCY"]]
    return filtered_data_df


def derive_frequency_matrix(data_df):
    """
    Function to derive frequency matrix
    :param data_df:
    :return:
    """

    column_rename_dictionary = {"INVOICE_DATE": "FREQUENCY"}
    filtered_data_df = data_df[["CUSTOMER_ID", "INVOICE_DATE"]]
    filtered_data_df = filtered_data_df.drop_duplicates()
    filtered_data_df = filtered_data_df.groupby(by=["CUSTOMER_ID"]).count().reset_index()
    filtered_data_df = filtered_data_df.rename(columns=column_rename_dictionary)
    return filtered_data_df


def derive_monetary_matrix(data_df):
    """
    Function
    :param data_df:
    :return:
    """

    column_rename_dictionary = {"INVOICE_DATE": "FREQUENCY"}
    filtered_data_df = data_df[["CUSTOMER_ID", "PURCHASE_COST"]]
    filtered_data_df = filtered_data_df.groupby(by=["CUSTOMER_ID"]).sum().reset_index()
    filtered_data_df = filtered_data_df.rename(columns=column_rename_dictionary)
    return filtered_data_df


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


def perform_rfm_analysis(read_from_csv=True, data_set_name=None, reference_date=None):
    """
    Function to perform RFM Analysis
    :param reference_date:
    :param data_set_name:
    :param read_from_csv:
    :return: RFM Analysis DataFrame
    """
    complete_retail_data = load_online_retail_data(read_from_csv)
    relevant_data_df = complete_retail_data.get(data_set_name)
    processed_data_df = clean_online_retail_data(relevant_data_df)

    # Perform Each one of the RFM analysis
    recency_df = derive_recency_matrix(processed_data_df, reference_date)
    monetary_df = derive_monetary_matrix(processed_data_df)
    frequency_df = derive_frequency_matrix(processed_data_df)

    recency_df = recency_df.merge(monetary_df, on=["CUSTOMER_ID"])
    final_df = recency_df.merge(frequency_df, on="CUSTOMER_ID")
    return final_df


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

    data_df = perform_rfm_analysis(read_from_csv=True, data_set_name="complete_retail_data", reference_date="01/01/2011")
    visualize_recency_matrix(data_df)


if __name__ == '__main__':
    main()

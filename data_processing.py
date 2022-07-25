import pandas as pd


def format_complete_retail_data(complete_data):
    """
    Function to format the complete retail data
    :param complete_data:
    :return:
    """
    column_rename_dictionary = {"Invoice": "INVOICE_NUMBER", "StockCode": "STOCK_CODE",
                                "Description": "PRODUCT_DESCRIPTION", "Quantity": "QUANTITY",
                                "InvoiceDate": "INVOICE_DATE", "Price": "PRICE", "Customer ID": "CUSTOMER_ID",
                                "Country": "COUNTRY"}

    data_df = pd.DataFrame()
    for sheet_name in complete_data:
        data_df = data_df.append(complete_data.get(sheet_name))

    data_df = data_df.rename(columns=column_rename_dictionary)
    return data_df


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

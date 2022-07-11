def format_complete_retail_data(complete_data):
    """
    Function to format the complete retail data
    :param data_df:
    :return:
    """
    import pandas as pd
    column_rename_dictionary = {"Invoice": "INVOICE_NUMBER", "StockCode": "STOCK_CODE",
                                "Description": "PRODUCT_DESCRIPTION", "Quantity": "QUANTITY",
                                "InvoiceDate": "INVOICE_DATE", "Price": "PRICE", "Customer ID": "CUSTOMER_ID",
                                "Country": "COUNTRY"}

    data_df = pd.DataFrame()
    for sheet_name in complete_data:
        data_df = data_df.append(complete_data.get(sheet_name))

    data_df = data_df.rename(columns=column_rename_dictionary)
    return data_df


FILE_BASED_CONFIG = {"complete_retail_data": {"file_name": "online_retail_II_sample.xlsx", "skiprows": 0, "skipfooter": 0,
                                              "sheet_name": None, "format_function": format_complete_retail_data}
                     }


MYSQL_BASED_CONFIG = {"table_1_1": {"SQL_QUERY": ""}}

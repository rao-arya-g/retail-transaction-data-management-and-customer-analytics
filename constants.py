from utility_functions import format_complete_retail_data


FILE_BASED_CONFIG = {"complete_retail_data": {"file_name": "online_retail_II_sample.xlsx", "skiprows": 0, "skipfooter": 0,
                                              "sheet_name": None, "format_function": format_complete_retail_data}
                     }


MYSQL_BASED_CONFIG = {"table_1_1": {"SQL_QUERY": ""}}

BASE_FREQUENCY_BINS = [0, 2, 5, 10]
FREQUENCY_LABELS = [1, 2, 3, 4]

BASE_RECENCY_BINS = [0, 2, 5, 10]
RECENCY_LABELS = [1, 2, 3, 4]

BASE_MONETARY_BINS = [0, 2, 5, 10]
MONETARY_LABELS = [1, 2, 3, 4]

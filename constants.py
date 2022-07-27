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

CATEGORY_MAP = {'Champion': {'RECENCY_SCORE': ['2', '3', '4'], 'FREQUENCY_SCORE': ['4'], 'MONETARY_SCORE': ['4']},
                'Top Loyal Customer': {'RECENCY_SCORE': ['3'], 'FREQUENCY_SCORE': ['1', '2', '3', '4'], 'MONETARY_SCORE': ['3', '4']},
                'Loyal Customer': {'RECENCY_SCORE': ['3'], 'FREQUENCY_SCORE': ['1', '2', '3', '4'], 'MONETARY_SCORE': ['1', '2']},
                'Top Recent Customer': {'RECENCY_SCORE': ['4'], 'FREQUENCY_SCORE': ['1', '2', '3', '4'], 'MONETARY_SCORE': ['3', '4']},
                'Recent Customer': {'RECENCY_SCORE': ['4'], 'FREQUENCY_SCORE': ['1', '2', '3', '4'], 'MONETARY_SCORE': ['1', '2']},
                'Top Customer Needed Attention': {'RECENCY_SCORE': ['2', '3'], 'FREQUENCY_SCORE': ['1', '2', '3', '4'], 'MONETARY_SCORE': ['3', '4']},
                'Customer Needed Attention': {'RECENCY_SCORE': ['2', '3'], 'FREQUENCY_SCORE': ['1', '2', '3', '4'], 'MONETARY_SCORE': ['1', '2']},
                'Top Lost Customer': {'RECENCY_SCORE': ['1'], 'FREQUENCY_SCORE': ['1', '2', '3', '4'], 'MONETARY_SCORE': ['3', '4']},
                'Lost Customer': {'RECENCY_SCORE': ['1'], 'FREQUENCY_SCORE': ['1', '2', '3', '4'], 'MONETARY_SCORE': ['1', '2']},
                }

from constants import CATEGORY_MAP


def allocate_total_rfm_score(data_df):
    """
    Function to allocate the total RFM score. The function combines all the 3 scores - one as Strings and other one as Integers
    :param data_df: Input DataFrame with score for Recency, Frequency, and Monetary.
    :return: Processed DataFrame with Total Score and Total RFM Label.
    """

    data_df['TOTAL_RFM_SCORE'] = data_df['RECENCY_SCORE'] + data_df['FREQUENCY_SCORE'] + data_df['MONETARY_SCORE']
    data_df['TOTAL_RFM_LABEL'] = data_df['RECENCY_SCORE'].astype(int) + data_df['FREQUENCY_SCORE'].astype(int) + data_df['MONETARY_SCORE'].astype(int)
    return data_df


def categorize_customers(row):
    """
    Function to categorize the customers based on the Category and Scores for each of the metrices
    :param row: Input DataFrame with score for Recency, Frequency, and Monetary.
    :return: Processed DataFrame with Customer category.
    """

    for key in CATEGORY_MAP:
        score_map = CATEGORY_MAP[key]
        if row['RECENCY_SCORE'] in score_map['RECENCY_SCORE'] and row['FREQUENCY_SCORE'] in score_map['FREQUENCY_SCORE'] and row['MONETARY_SCORE'] in score_map['MONETARY_SCORE']:
            return key

    return 'NOT_CATEGORIZED'

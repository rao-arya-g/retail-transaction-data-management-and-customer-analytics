def get_high_level_customer_info(data_df):
    """
    Function to get the high level customer information
    :param data_df:
    :return:
    """
    print(data_df.describe())
    return data_df


def allocate_total_rfm_score(data_df):
    """
    Function to allocate the total RFM score
    :param data_df:
    :return:
    """
    data_df['TOTAL_RFM_SCORE'] = data_df.apply(lambda x: str(int(x['RECENCY_SCORE'])) + str(int(x['FREQUENCY_SCORE'])) + str(int(x['MONETARY_SCORE'])), axis=1)
    data_df['TOTAL_RFM_LABEL'] = data_df['RECENCY_SCORE'] + data_df['FREQUENCY_SCORE'] + data_df['MONETARY_SCORE']
    return data_df


def perform_customer_segmentation(data_df):
    """
    Function to do something
    :param data_df:
    :return:
    """

    return data_df

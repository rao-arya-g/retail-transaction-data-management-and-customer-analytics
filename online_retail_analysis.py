from assoication_rule_mining import get_data_for_arm, perform_arm_apriori
from customer_segmentation import get_high_level_customer_info, allocate_total_rfm_score
from data_processing import clean_online_retail_data, load_online_retail_data
# from online_retail_visualization import visualize_recency_matrix
from rfm_analysis import derive_recency_matrix, derive_monetary_matrix, derive_frequency_matrix, allocate_rfm_scores


def perform_rfm_analysis(data_set_name=None, reference_date=None, read_from_csv=True):
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
    final_df = allocate_rfm_scores(final_df)
    return final_df


def perform_association_rule_mining(data_set_name=None, read_from_csv=True):
    complete_retail_data = load_online_retail_data(read_from_csv)
    relevant_data_df = complete_retail_data.get(data_set_name)
    processed_data_df = clean_online_retail_data(relevant_data_df)
    processed_data_df = get_data_for_arm(processed_data_df)
    perform_arm_apriori(processed_data_df)


def main():
    """
    Main method - Present now to test few things
    :return: None
    """
    reference_date = "01/01/2011"
    data_set_name = "complete_retail_data"
    data_df = perform_rfm_analysis(data_set_name=data_set_name, reference_date=reference_date, read_from_csv=True)
    get_high_level_customer_info(data_df)
    data_df = allocate_total_rfm_score(data_df)
    data_df.to_clipboard()

    # perform_association_rule_mining(data_set_name=data_set_name, read_from_csv=True)
    # visualize_recency_matrix(data_df)


if __name__ == '__main__':
    main()

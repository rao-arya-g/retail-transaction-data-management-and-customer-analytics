from assoication_rule_mining import get_data_for_arm, perform_arm_apriori, perform_arm_fpgrowth
from customer_segmentation import allocate_total_rfm_score, categorize_customers
from data_processing import clean_online_retail_data, load_online_retail_data
from online_retail_visualization import visualize_recency_matrix, display_basic_data_info, \
    visualize_expensive_goods_distribution, visualize_sales_trend, visualize_recency_score_distribution, visualize_customer_category
from rfm_analysis import derive_recency_matrix, derive_monetary_matrix, derive_frequency_matrix, allocate_rfm_scores


def perform_rfm_analysis(data_set_name=None, reference_date=None, read_from_csv=True):
    """
    Function to perform RFM Analysis
    :param reference_date:
    :param data_set_name: Data set name on which association rule mining is performed.
    :param read_from_csv: Boolean flag to indicate whether reading should be done from csv or from MySQL.
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
    visualize_recency_matrix(final_df)
    return final_df


def perform_customer_segmentation(data_set_name=None, reference_date=None, read_from_csv=True):
    """
    Function to do something
    :param read_from_csv: Boolean flag to indicate whether reading should be done from csv or from MySQL.
    :param reference_date:
    :param data_set_name: Data set name on which association rule mining is performed.
    :return:
    """
    data_df = perform_rfm_analysis(data_set_name=data_set_name, reference_date=reference_date, read_from_csv=read_from_csv)
    data_df = allocate_total_rfm_score(data_df)
    data_df['CUSTOMER_CATEGORY'] = data_df.apply(categorize_customers, axis=1)
    visualize_recency_score_distribution(data_df)
    visualize_customer_category(data_df)


def perform_association_rule_mining(data_set_name=None, read_from_csv=True, apriori=True):
    """
    Function to perform Association rule mining.
    :param data_set_name: Data set name on which association rule mining is performed.
    :param read_from_csv: Boolean flag to indicate whether reading should be done from csv or from MySQL.
    :param apriori: Indicate whether to use Apriori or FPGrowth algorithm.
    :return: Association rules
    """
    complete_retail_data = load_online_retail_data(read_from_csv)
    relevant_data_df = complete_retail_data.get(data_set_name)
    processed_data_df = clean_online_retail_data(relevant_data_df)
    processed_data_df = get_data_for_arm(processed_data_df)
    if apriori:
        rules = perform_arm_apriori(processed_data_df)
    else:
        rules = perform_arm_fpgrowth(processed_data_df)
    return rules


def perform_basic_data_set_display(data_set_name=None, read_from_csv=True):
    """
    Function to perform basic data set display
    :param data_set_name: Data set name on which association rule mining is performed.
    :param read_from_csv: Boolean flag to indicate whether reading should be done from csv or from MySQL.
    :return:
    """
    complete_retail_data = load_online_retail_data(read_from_csv)
    relevant_data_df = complete_retail_data.get(data_set_name)
    display_basic_data_info(relevant_data_df)


def perform_sales_analysis(data_set_name=None, read_from_csv=True):
    """
    Function to perform sales analysis
    :param data_set_name: Data set name on which association rule mining is performed.
    :param read_from_csv: Boolean flag to indicate whether reading should be done from csv or from MySQL.
    :return:
    """
    complete_retail_data = load_online_retail_data(read_from_csv)
    relevant_data_df = complete_retail_data.get(data_set_name)
    relevant_data_df = clean_online_retail_data(relevant_data_df)
    visualize_expensive_goods_distribution(relevant_data_df)
    visualize_sales_trend(relevant_data_df)


def main():
    """
    Main method - Present now to test few things
    :return: None
    """
    reference_date = "01/01/2012"
    data_set_name = "complete_retail_data"
    read_from_csv = True

    data_df = perform_rfm_analysis(data_set_name=data_set_name, reference_date=reference_date, read_from_csv=read_from_csv)
    perform_customer_segmentation(data_df)


if __name__ == '__main__':
    main()

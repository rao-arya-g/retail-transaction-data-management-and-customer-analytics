from mlxtend.frequent_patterns import association_rules, apriori, fpgrowth

"""
Author: Arya Girisha Rao(ar1422@rit.edu)

This is a python file for Association rule mining module
"""


def get_data_for_arm(data_df):
    """
    Function to process the input data as per the requirement for Association rule mining.
    :param data_df: Input data df - Processed and filtered.
    :return: Processed Input data in the required format.
    """
    data_df = data_df.groupby(['INVOICE_NUMBER', 'PRODUCT_DESCRIPTION'])["QUANTITY"].sum().unstack().reset_index().fillna(0).set_index("INVOICE_NUMBER")

    def encode_values(x):
        if x <= 0:
            return 0
        if x >= 1:
            return 1

    data_df = data_df.applymap(encode_values)
    data_df = data_df[(data_df > 0).sum(axis=1) >= 2]
    return data_df


def perform_arm_apriori(data_df):
    """
    Function to perform Association rule mining using Apriori algorithm.
    :param data_df: Input data processed and in the required format.
    :return: Derived association rules
    """

    freq_items = apriori(data_df, min_support=0.02, use_colnames=True).sort_values(by='support', ascending=False)
    rules = association_rules(freq_items, metric='lift', min_threshold=1).sort_values(by='lift', ascending=False)
    rules = rules[(rules['lift'] > 5) & (rules['confidence'] > 0.5)]
    return rules


def perform_arm_fpgrowth(data_df):
    """
    Function to perform Association rule mining using FPGrowth algorithm.
    :param data_df: Input data processed and in the required format.
    :return:Derived association rules
    """

    freq_items1 = fpgrowth(data_df, min_support=0.02, use_colnames=True).sort_values(by='SUPPORT', ascending=False)
    rules1 = association_rules(freq_items1, metric='lift', min_threshold=1).sort_values(by='LIFT', ascending=False)
    rules1 = rules1[(rules1['LIFT'] > 5) & (rules1['CONFIDENCE'] > 0.5)]
    return rules1

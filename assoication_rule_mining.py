import pandas as pd
from mlxtend.frequent_patterns import association_rules, apriori, fpgrowth


def get_data_for_arm(data_df):
    """
    Function to do something.
    :param data_df:
    :return:
    """
    data_df = data_df.sort_values(by='INVOICE_DATE')
    data_df = data_df.set_index('INVOICE_DATE')
    data_df['SOLD'] = 1
    pivoted_data_df = pd.pivot_table(data_df, values=['SOLD'], index=['INVOICE_DATE'], columns=['PRODUCT_DESCRIPTION']).fillna(0)
    return pivoted_data_df


def perform_arm_apriori(data_df):
    """

    :param data_df:
    :return:
    """
    freq_items = apriori(data_df, min_support=0.02, use_colnames=True).sort_values(by='SUPPORT', ascending=False)
    rules = association_rules(freq_items, metric='LIFT', min_threshold=1).sort_values(by='LIFT', ascending=False)
    rules = rules[(rules['LIFT'] > 5) & (rules['CONFIDENCE'] > 0.5)]
    return rules


def perform_arm_fpgrowth(data_df):
    """
    Function
    :param data_df:
    :return:
    """

    freq_items1 = fpgrowth(data_df, min_support=0.02, use_colnames=True).sort_values(by='SUPPORT', ascending=False)
    rules1 = association_rules(freq_items1, metric='lift', min_threshold=1).sort_values(by='LIFT', ascending=False)
    rules1 = rules1[(rules1['LIFT'] > 5) & (rules1['CONFIDENCE'] > 0.5)]
    return rules1

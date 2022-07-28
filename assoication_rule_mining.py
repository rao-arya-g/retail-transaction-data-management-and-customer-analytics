from mlxtend.frequent_patterns import association_rules, apriori, fpgrowth


def get_data_for_arm(data_df):
    """
    Function to do something.
    :param data_df:
    :return:
    """
    data_df = data_df[data_df['COUNTRY'] == "United Kingdom"].groupby(['INVOICE_NUMBER', 'PRODUCT_DESCRIPTION'])["QUANTITY"].sum().unstack().reset_index().fillna(0).set_index("INVOICE_NUMBER")

    def encode_values(x):
        if x <= 0:
            return 0
        if x >= 1:
            return 1

    # Apply function to data
    data_df = data_df.applymap(encode_values)
    data_df = data_df[(data_df > 0).sum(axis=1) >= 2]
    return data_df


def perform_arm_apriori(data_df):
    """

    :param data_df:
    :return:
    """

    freq_items = apriori(data_df, min_support=0.02, use_colnames=True).sort_values(by='support', ascending=False)
    rules = association_rules(freq_items, metric='lift', min_threshold=1).sort_values(by='lift', ascending=False)
    rules = rules[(rules['lift'] > 5) & (rules['confidence'] > 0.5)]
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

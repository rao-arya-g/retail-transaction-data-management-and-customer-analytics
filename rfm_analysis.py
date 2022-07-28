import datetime
import pandas as pd
from constants import FREQUENCY_LABELS, BASE_FREQUENCY_BINS, BASE_MONETARY_BINS, BASE_RECENCY_BINS, \
    RECENCY_LABELS, MONETARY_LABELS


def derive_monetary_matrix(data_df):
    """
    Function
    :param data_df:
    :return:
    """

    column_rename_dictionary = {"PURCHASE_COST": "MONETARY"}
    filtered_data_df = data_df[["CUSTOMER_ID", "PURCHASE_COST"]]
    filtered_data_df = filtered_data_df.groupby(by=["CUSTOMER_ID"]).sum().reset_index()
    filtered_data_df = filtered_data_df.rename(columns=column_rename_dictionary)
    return filtered_data_df


def allocate_rfm_scores(data_df):
    """
    Function to allocate score for RFM.
    :param data_df:
    :return:
    """

    data_df['FREQUENCY_SCORE'] = pd.cut(data_df['FREQUENCY'], bins=BASE_FREQUENCY_BINS+[max(data_df['FREQUENCY']+1)],
                                        labels=FREQUENCY_LABELS).astype(str)

    data_df['RECENCY_SCORE'] = pd.cut(data_df['RECENCY'], bins=BASE_RECENCY_BINS+[max(data_df['RECENCY']+1)],
                                      labels=RECENCY_LABELS).astype(str)

    data_df['MONETARY_SCORE'] = pd.cut(data_df['MONETARY'], bins=BASE_MONETARY_BINS+[max(data_df['MONETARY']+1)],
                                       labels=MONETARY_LABELS).astype(str)

    return data_df


def derive_recency_matrix(data_df, reference_date=None):
    """
    Function to derive recency matrix
    :param data_df:
    :param reference_date:
    :return:
    """

    if reference_date is not None and isinstance(reference_date, str):
        reference_date = datetime.datetime.strptime(reference_date, "%m/%d/%Y").date()
    else:
        reference_date = datetime.datetime.now().date()

    data_df["INVOICE_DATE_ONLY"] = data_df["INVOICE_DATE"].apply(lambda x: x.date())
    filtered_data_df = data_df[["CUSTOMER_ID", "INVOICE_DATE_ONLY"]]
    filtered_data_df = filtered_data_df.groupby(by=["CUSTOMER_ID"]).max().reset_index()
    filtered_data_df['RECENCY'] = filtered_data_df['INVOICE_DATE_ONLY'].apply(lambda x: (reference_date - x).days)
    filtered_data_df = filtered_data_df[["CUSTOMER_ID", "RECENCY"]]
    return filtered_data_df


def derive_frequency_matrix(data_df):
    """
    Function to derive frequency matrix.
    :param data_df:
    :return:
    """

    column_rename_dictionary = {"INVOICE_DATE": "FREQUENCY"}
    filtered_data_df = data_df[["CUSTOMER_ID", "INVOICE_DATE"]]
    filtered_data_df = filtered_data_df.drop_duplicates()
    filtered_data_df = filtered_data_df.groupby(by=["CUSTOMER_ID"]).count().reset_index()
    filtered_data_df = filtered_data_df.rename(columns=column_rename_dictionary)
    return filtered_data_df

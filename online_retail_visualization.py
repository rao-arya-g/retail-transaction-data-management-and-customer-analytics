import matplotlib.pyplot as plt


def visualize_recency_matrix(data_df):
    """
    Function to visualize the recency matrix
    :param data_df: DataFrame of the Customers with recent buy matrix information.
    :return: None
    """

    plt.hist(data_df["RECENCY"], bins=52)
    plt.title("Trend of Customers buying pattern in terms of recency")
    font = {'family': 'serif', 'color': 'darkred', 'weight': 'normal', 'size': 12}

    plt.xlabel("Number of days since purchasing", fontdict=font)
    plt.ylabel("Number of customers", fontdict=font)
    plt.show()


def visualize_monetary_matrix(data_df):
    """
    Function to visualize the monetary matrix
    :param data_df: DataFrame of the Customers with recent buy matrix information.
    :return: None
    """

    plt.hist(data_df["MONETARY"], bins=52)
    plt.title("Trend of Customers buying pattern in terms of money")
    font = {'family': 'serif', 'color': 'darkred', 'weight': 'normal', 'size': 12}

    plt.xlabel("Money spent by the customers", fontdict=font)
    plt.ylabel("Number of customers", fontdict=font)
    plt.show()


def visualize_frequency_matrix(data_df):
    """

    :param data_df:
    :return:
    """
    return data_df


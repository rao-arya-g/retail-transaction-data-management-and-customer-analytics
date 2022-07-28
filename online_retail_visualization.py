import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
sns.set(style="darkgrid")


def display_basic_data_info(data_df):
    """
    Function to display basic information about the Data set.
    :param data_df: Data set in DataFrame format.
    :return: None
    """

    # Basic Data set information messages
    total_rows_message = "Number of rows in the Data set is: {}"
    total_cols_message = "Number of columns in Data set is: {}"
    total_users_message = "Number of unique Customers in the Data set is: {}"

    print(total_rows_message.format(data_df.shape[0]))
    print(total_cols_message.format(data_df.shape[1]))
    print(total_users_message.format(len(data_df['CUSTOMER_ID'].unique().tolist())))

    # Filtered information
    cancelled_transaction_message = "Number of cancelled transactions: {}"
    pct_of_cancelled_transaction_message = "Percentage of cancelled transactions: {}"

    cancelled = data_df[data_df['INVOICE_NUMBER'].astype(str).str.contains('C')]
    print(cancelled_transaction_message.format(len(cancelled)))
    print(pct_of_cancelled_transaction_message.format(round(len(cancelled) / len(data_df) * 100, 2), "%"))

    # Retained Data set information
    negative_quantity_message = "Number of transactions with negative quantity value among valid transactions: {}"
    zero_price_message = "Number of transactions with zero price and negative quantity: {}"
    zero_price_pct_message = "Percentage of transactions with zero or negative price: {}"
    duplicate_transaction_message = "Number of duplicated transactions: {}"

    non_cancelled = data_df[~data_df['INVOICE_NUMBER'].astype(str).str.contains('C')]
    data_df = data_df[(data_df['PRICE'] > 0) & (data_df['QUANTITY'] > 0)]

    print(negative_quantity_message.format(len(non_cancelled[non_cancelled['QUANTITY'] <= 0])))
    print(zero_price_message.format(len(non_cancelled[(non_cancelled['QUANTITY'] <= 0) & (non_cancelled['PRICE'] == 0)])))
    print(zero_price_pct_message.format(round(len(data_df[data_df['PRICE'] <= 0]) / len(data_df) * 100, 2), "%"))
    print(duplicate_transaction_message.format(len(data_df[data_df.duplicated()])))


def frequently_purchased_items(data_df, limit=20):
    """
    Function to visualize frequently purchased items
    :param limit:
    :param data_df:
    :return:
    """

    prod = pd.DataFrame(data_df['PRODUCT_DESCRIPTION'].value_counts()).sort_values(by='PRODUCT_DESCRIPTION', ascending=False)
    prod = prod.head(limit)
    plt.figure(figsize=(10, 5))
    plt.barh(prod.index, prod.PRODUCT_DESCRIPTION, color='#187bc8')
    plt.xlabel('Number of times purchased')
    plt.title('Frequently Purchased Products')
    plt.show()


def new_function(data_df):
    data_df['MONTH'] = data_df['INVOICE_DATE'].dt.month
    data_df['YEAR'] = data_df['INVOICE_DATE'].dt.year
    data_df['WEEKDAY'] = data_df['INVOICE_DATE'].dt.day_name()
    data_df['MONTH_YEAR'] = pd.to_datetime(data_df[['YEAR', 'MONTH']].assign(Day=1))
    data_df['HOUR'] = data_df['INVOICE_DATE'].dt.hour

    plot1 = pd.DataFrame(data_df.groupby(['MONTH_YEAR'])['INVOICE_NUMBER'].count()).reset_index()
    plot2 = pd.DataFrame(data_df.groupby(['WEEKDAY'])['INVOICE_NUMBER'].count())
    plot3 = pd.DataFrame(data_df.groupby(['HOUR'])['INVOICE_NUMBER'].count()).reset_index()
    plot4 = pd.DataFrame(data_df.groupby(['MONTH_YEAR'])['PURCHASE_COST'].mean()).reset_index()
    plot5 = pd.DataFrame(data_df.groupby(['MONTH_YEAR'])['PURCHASE_COST'].sum()).reset_index()
    plot2 = plot2.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday']).reset_index()

    ax = sns.lineplot(x="MONTH_YEAR", y="INVOICE_NUMBER", data=plot1).set(title='orders per month')
    ax = sns.barplot(x="WEEKDAY", y="INVOICE_NUMBER", data=plot2).set(title='orders per day')
    ax = sns.barplot(x="HOUR", y="INVOICE_NUMBER", data=plot3).set(title='orders per hour')
    ax = sns.lineplot(x='MONTH_YEAR', y='PURCHASE_COST', data=plot5).set(title='month that brings the highest revenue')

    plt.show()


def another_stupid_function(data_df):
    """

    :param data_df:
    :return:
    """
    sns.distplot(data_df[data_df['PRICE'] > 50]['PRICE'], kde=False, rug=True).set(title='Price distribution of expensive goods')


def country_related_stuff(data_df):
    """

    :param data_df:
    :return:
    """
    customer_country = data_df[['Country', 'CustomerID']].drop_duplicates()
    customer_country.groupby(['Country'])['CustomerID'].aggregate('count').reset_index().sort_values('CustomerID', ascending=False)
    print("Transactions were made in", len(data_df['Country'].unique().tolist()), "different countries")
    print("Number of transactions where country is unspecified:", len(data_df[data_df['Country'] == 'Unspecified']))
    plot6 = pd.DataFrame(data_df.groupby(['Country'])['revenue'].sum()).reset_index()
    plot6 = plot6.sort_values(['revenue']).reset_index(drop=True)
    plot7 = pd.DataFrame(data_df.groupby(['Country'])['revenue'].count()).reset_index()
    plot7 = plot7.sort_values(['revenue']).reset_index(drop=True)
    fig, ax = plt.subplots()
    fig.set_size_inches(13, 11.5)
    ax = sns.barplot(x='Country', y='revenue', data=plot6.tail(10), estimator=max, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=47, ha="right")
    plt.show()


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


import pandas as pd

orders = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/orders.csv')
customers = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/customers.csv',
                       parse_dates=['birth_date'])

merged = customers.merge(orders, on='customer_id')
orders_1990 = merged[
    merged['birth_date'].dt.year == 1990
][['order_id', 'customer_id']]

print(orders_1990)
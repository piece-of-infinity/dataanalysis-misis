import pandas as pd

orders = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/orders.csv', 
                    parse_dates=['order_date'])
customers = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/customers.csv')

merged = customers.merge(orders, on='customer_id')
russian_orders = merged[
    (merged['customer_id'].between(68, 88)) & 
    (merged['order_date'].dt.year == 2022)
].iloc[4:10][['order_id', 'total']]

print(russian_orders)
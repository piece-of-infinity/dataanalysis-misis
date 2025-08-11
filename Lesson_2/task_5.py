import pandas as pd

orders = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/orders.csv')

filtered_orders = orders[
    (orders['customer_id'].between(10, 20)) & 
    (orders['total'] > 8000)
][['order_id', 'customer_id', 'total']]

print(filtered_orders)
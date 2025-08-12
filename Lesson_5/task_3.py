import pandas as pd

orders = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/orders_new.csv')

product_counts = orders.groupby('product')['order_id'].nunique().reset_index(name='order_count')
print(product_counts)
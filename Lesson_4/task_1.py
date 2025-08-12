import pandas as pd

df = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/group_orders.csv')

orders_count = df.groupby('city')['order_id'].count().reset_index(name='orders_count')
print(orders_count)

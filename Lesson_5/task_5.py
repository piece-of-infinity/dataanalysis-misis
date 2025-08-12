import pandas as pd

orders = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/orders_new.csv')
users = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/users_new.csv')

order_counts = orders.groupby('user_id')['order_id'].nunique().reset_index(name='orders_count')

multi_orders = order_counts[order_counts['orders_count'] > 1]

result = multi_orders.merge(users[['user_id', 'name']], on='user_id', how='left')
print(result[['name', 'orders_count']])

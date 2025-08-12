import pandas as pd

users = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/users_new.csv')
orders = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/orders_new.csv')

north_users = users[(users['region'] == 'North') & (users['age'] < 30)]

merged = orders.merge(north_users, on='user_id', how='inner')

order_counts = merged.groupby(['name'])['order_id'].nunique().reset_index(name='order_count')

print(order_counts)
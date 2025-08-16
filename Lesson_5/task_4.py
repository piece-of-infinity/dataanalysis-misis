import pandas as pd

users = pd.read_csv('../All_Files/users_new.csv')
orders = pd.read_csv('../All_Files/orders_new.csv')

merged = orders.merge(users, on='user_id', how='left')

merged['total'] = merged['price'] * merged['quantity']

pivot = merged.pivot_table(
    index='region',
    columns='product',
    values='total',
    aggfunc='sum'
)

print(pivot)
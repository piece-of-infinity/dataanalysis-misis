import pandas as pd

orders = pd.read_csv('All_Files/orders.csv', parse_dates=['order_date'])

filtered_orders = orders[
    (orders['total'].between(30000, 40000)) & 
    (orders['order_date'] >= '2023-01-01')
][['order_id']]

print(filtered_orders)
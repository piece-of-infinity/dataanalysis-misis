import pandas as pd

orders = pd.read_csv(
    '/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/orders.csv',
    parse_dates=['order_date']
)
orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')

result = orders[
    (orders['total'].between(10000, 15000)) & 
    (orders['order_date'].dt.year == 2023)
][['order_id', 'total', 'order_date']]

print(result)
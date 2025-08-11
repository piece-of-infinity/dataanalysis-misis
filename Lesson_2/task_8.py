import pandas as pd

orders = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/orders.csv',
                    parse_dates=['order_date'])

orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')

feb_2023_orders = orders[
    (orders['order_date'].dt.year == 2023) & 
    (orders['order_date'].dt.month == 2) & 
    (orders['total'] > 5000)
]

print(feb_2023_orders)
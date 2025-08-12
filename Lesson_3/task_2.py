import pandas as pd

contacts = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/contacts.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/orders.csv', sep=',', encoding='utf-8')

df = contacts.merge(customers, how='right', on='customer_id') \
             .merge(orders, how='inner', on='customer_id')

df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

filtered = df.query(
    "registration_date.dt.year >= 2022 and order_date.dt.year == 2023 and total > 30000"
)[['first_name','last_name', 'total']]

print(filtered)
print("Количество таких продаж:", filtered.shape[0])
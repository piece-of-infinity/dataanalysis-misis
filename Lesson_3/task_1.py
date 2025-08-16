import pandas as pd

# Загрузка данных
contacts = pd.read_csv('../All_Files/contacts.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('../All_Files/customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('../All_Files/orders.csv', sep=',', encoding='utf-8')

# Объединение таблиц (inner join с заказами)
df = contacts.merge(customers, how='right', on='customer_id') \
             .merge(orders, how='inner', on='customer_id')

# Приведение даты к формату datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Европейские страны + Россия из реальных данных
europe_countries = ['Russia', 'Italy', 'Spain', 'UK', 'France', 'Germany']

# Фильтрация: Европа/Россия, первые 2 квартала 2023 года
filtered_df = df.loc[
    (df['country'].isin(europe_countries)) &
    (df['order_date'].dt.year == 2023) &
    (df['order_date'].dt.quarter <= 2),
    ['order_id', 'total']
]

# Вывод результата
print(filtered_df)
print("Сумма продаж:", filtered_df['total'].sum())


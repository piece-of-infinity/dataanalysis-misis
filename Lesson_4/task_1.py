import pandas as pd

df = pd.read_csv('../All_Files/group_orders.csv')

orders_count = df.groupby('city')['order_id'].count().reset_index(name='orders_count')
print("Кол-во заказов по городам:")
print(orders_count) 

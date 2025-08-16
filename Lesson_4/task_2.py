import pandas as pd

df = pd.read_csv('../All_Files/group_orders.csv')

avg_order_sum = df.groupby('city')['total'].mean().reset_index(name='avg_total')
print("Средняя сумма заказа по городам:")
print(avg_order_sum)

import pandas as pd

df = pd.read_csv('../All_Files/group_orders.csv')

top3_cities = df.groupby('city')['total'].mean().reset_index(name='avg_order_total')
top3_cities = top3_cities.sort_values(by='avg_order_total', ascending=False).head(3)
print("Топ-3 города по средней сумме заказа:")
print(top3_cities)

import pandas as pd

df = pd.read_csv('../All_Files/group_orders.csv')

total_quantity = df.groupby('product')['quantity'].sum().reset_index()
total_quantity = total_quantity.sort_values(by='quantity', ascending=False).head(1)
print("Самый популярный товар по количеству:")
print(total_quantity)

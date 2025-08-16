import pandas as pd

orders = pd.read_csv('../All_Files/orders_new.csv')

orders['total'] = orders['price'] * orders['quantity']

result = orders.query("product == 'C' and total > 250")

print(result[['order_id', 'user_id', 'product', 'price', 'quantity', 'order_date', 'total']])
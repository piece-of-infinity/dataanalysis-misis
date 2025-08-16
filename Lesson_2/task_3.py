import pandas as pd

products = pd.read_csv('../All_Files/products.csv')

filtered_products = products[
    (products['price'] < 500) & 
    (products['volume_ml'] == 5.0)
][['product_name', 'price']]

print(filtered_products)
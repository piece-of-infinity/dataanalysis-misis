import pandas as pd

df = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/group_orders.csv')

df['order_date'] = pd.to_datetime(df['order_date'])

df['order_month'] = df['order_date'].dt.to_period('M')
monthly_revenue = df.groupby('order_month')['total'].sum().reset_index(name='monthly_revenue')
print("Общая выручка по месяцам:")
print(monthly_revenue)

import pandas as pd

def main():
    orders_path = '../All_Files/orders.csv'
    customers_path = '../All_Files/customers.csv'
    
    try:
        orders = pd.read_csv(orders_path, parse_dates=['order_date'])
        customers = pd.read_csv(customers_path)
        
        merged = pd.merge(customers, orders, on='customer_id')
        
        if not pd.api.types.is_datetime64_any_dtype(merged['order_date']):
            merged['order_date'] = pd.to_datetime(merged['order_date'], errors='coerce')
        
        result = merged[
            (merged['customer_id'].between(68, 88)) & 
            (merged['order_date'].dt.year == 2022)
        ].iloc[5:11][['order_id', 'total']]
        
        print("Результат:")
        print(result)
    
    except Exception as e:
        print(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    main()
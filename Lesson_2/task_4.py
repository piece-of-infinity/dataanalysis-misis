import pandas as pd

customers = pd.read_csv('/Users/snezana/misis_data_analysis/dataanalysis-misis/All_Files/customers.csv',
                       parse_dates=['birth_date'])

women_before_1995 = customers[
    (customers['gender'] == 'F') & 
    (customers['birth_date'].dt.year < 1995)
][['customer_id', 'first_name', 'last_name', 'birth_date']]

print(women_before_1995)
'''
Data Handling: Introduction to Pandas

Pandas is a Python library used for data manipulation and analysis.
Provides two key data structures:
    - DataFrame: 2D labeled data (like a table).
    - Series: 1D labeled data.


'''

import pandas as pd

# Load data from a CSV file
data = pd.read_csv('data.csv')
print(data.head())  # Display the first 5 rows of the data
print(data.tail())  # Display the last 5 rows of the data
print(data)
print(data['COMPANY NAME'])  # Display the 'COMPANY NAME' column
print(data['COMPANY NAME', 'customer name'])  # Display multiple columns

print(data['numbers'] > 10)


summary = data.describe()  # Summary statistics
print(summary)

avg = data['numbers'].mean()  # Calculate the mean of the 'numbers' column

sorted_data = data.sort_values('numbers', ascending=False)  # Sort the data by the 'numbers' column
print(sorted_data)

data['adding_companyname_and_customername'] = data['COMPANY NAME'] + data['customer name']

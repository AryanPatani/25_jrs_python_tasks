# Pandas
# Q1: Given a DataFrame df with columns: ["department", "employee", "salary"], 
#     normalize the salary within each department (i.e., for each department, subtract the mean and divide by the std of that department).
# Q2: Given a DataFrame with columns ["timestamp", "user_id", "action"], where timestamp is in string format, find the average number of actions per user per day.
# Q3: You have a DataFrame with columns: ["user_id", "product", "price", "quantity", "date"]. 
#     Calculate the total amount spent by each user on "Laptop" purchases only, 
#     and return the result as a new DataFrame with columns: ["user_id", "total_spent_on_laptops"].

import pandas as pd

# --------------------

df1 = pd.DataFrame({
    "department": ["HR","HR","IT","IT","IT"],
    "employee": ["Aryan","Kensei","Arthur","David","Trafalgar"],
    "salary": [50000,60000,65000,53000,75000]
})
df1['salary_normalized'] = (df1['salary'] - df1.groupby('department')['salary'].transform('mean')) / df1.groupby('department')['salary'].transform('std')
#print(df1)

# --------------------

df2 = pd.DataFrame({
    "timestamp": ["2023-01-01 10:00:00","2023-01-01 11:00:00","2023-01-02 08:00:00"],
    "user_id": [12,32,67],
    "action": ["click","view","edit"]
})
df2['date'] = pd.to_datetime(df2['timestamp']).dt.date
actions_per_user_day = df2.groupby(['user_id', 'date'])['action'].count().reset_index()
avg_actions = actions_per_user_day.groupby('user_id')['action'].mean().mean()
#print(avg_actions)

# --------------------
df3 = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 3],
    'product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Laptop'],
    'price': [1000, 20, 1200, 50, 1100],
    'quantity': [1, 2, 2, 1, 1],
    'date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03']
})
laptop_df = df3[df3['product'] == 'Laptop']
laptop_df['total'] = laptop_df['price'] * laptop_df['quantity']
result = laptop_df.groupby('user_id')['total'].sum().reset_index()
result.columns = ['user_id', 'total_spent_on_laptops']
print(result)
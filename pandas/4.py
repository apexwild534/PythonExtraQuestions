import pandas as pd

# Create the first DataFrame
data1 = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
}
df1 = pd.DataFrame(data1)

# Create the second DataFrame
data2 = {
    'ID': [2, 3, 4],
    'City': ['New York', 'Chicago', 'Los Angeles']
}
df2 = pd.DataFrame(data2)

# Merge the DataFrames based on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID')

# Print the merged DataFrame
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
print("\nMerged DataFrame:")
print(merged_df)

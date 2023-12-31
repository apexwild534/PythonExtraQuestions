import pandas as pd

# Create a dictionary for the DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'A'],
    'Value': [10, 20, 15, 25, 12, 18]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Group the data by 'Category' and calculate summary statistics
grouped_df = df.groupby('Category').agg({
    'Value': ['mean', 'sum', 'min', 'max', 'count']
}).reset_index()

# Rename the columns for clarity
grouped_df.columns = ['Category', 'Mean', 'Sum', 'Min', 'Max', 'Count']

# Print the grouped and aggregated DataFrame
print("Original DataFrame:")
print(df)
print("\nGrouped and Aggregated DataFrame:")
print(grouped_df)

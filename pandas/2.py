import pandas as pd

# Create a dictionary for the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 28, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Boston']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Set a threshold value for filtering
threshold = 25

# Filter rows where 'Age' is greater than the threshold
filtered_df = df[df['Age'] > threshold]

# Print the filtered DataFrame
print("Original DataFrame:")
print(df)
print("\nFiltered DataFrame (Age >", threshold, "):")
print(filtered_df)

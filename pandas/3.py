import pandas as pd

# Create a dictionary for the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 28, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Boston']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Specify the column for which you want to calculate mean and standard deviation
selected_column = 'Age'

# Calculate the mean and standard deviation
mean_value = df[selected_column].mean()
std_deviation = df[selected_column].std()

# Print the results
print("DataFrame:")
print(df)
print("\nMean of column '{}': {}".format(selected_column, mean_value))
print("Standard Deviation of column '{}': {}".format(selected_column, std_deviation))

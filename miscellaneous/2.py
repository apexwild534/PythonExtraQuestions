# Initialize the sum to 0
total = 0

# Loop through numbers from 1 to 100
for num in range(1, 101):
    if num % 2 == 0:  # Check if the number is even
        total += num

# Print the sum of even numbers
print("The sum of even numbers from 1 to 100 is:", total)

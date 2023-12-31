# This Python program calculates the sum of all numbers from 1 to n using a for loop.

# Get the value of n from the user.
n = int(input("Enter the value of n: "))

# Create a variable to store the sum of the numbers.
sum = 0

# Create a for loop that iterates over the numbers from 1 to n.
for i in range(1, n + 1):

    # Add the current number to the sum.
    sum += i

# Print the sum of the numbers.
print("The sum of the numbers from 1 to", n, "is", sum)
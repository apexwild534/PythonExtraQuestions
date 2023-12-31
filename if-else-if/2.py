# Input the user's age
age = int(input("Enter your age: "))

# Determine the age category and print a corresponding message
if age < 0:
    print("Invalid age. Please enter a non-negative number.")
elif age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")

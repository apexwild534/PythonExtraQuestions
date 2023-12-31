import random

# Generate a random target number between 1 and 100
target_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    user_guess = int(input("Take a guess: "))
    attempts += 1

    if user_guess < target_number:
        print("Too low! Try again.")
    elif user_guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
        break

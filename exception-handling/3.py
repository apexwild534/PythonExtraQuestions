def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Please enter an integer.")
    user_input = get_integer_input("Enter a number: ")
    print(f"You entered the integer: {user_input}")

if __name__ == "__main__":
    main()
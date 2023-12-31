# Define the initial game state
current_room = "Entrance"
inventory = []

# Define the game's map (rooms and their connections)
game_map = {
    "Entrance": {"description": "You are at the entrance of a mysterious cave. A path leads deeper into the cave.", "options": ["Go inside", "Quit"]},
    "Cave": {"description": "You find yourself in a dimly lit cave. There's a treasure chest in the corner.", "options": ["Open chest", "Go back"]},
    "Treasure Room": {"description": "You've discovered a room full of treasure! You win!", "options": ["Play again"]},
}

# Game loop
while True:
    # Display the current room's description
    print("\n" + game_map[current_room]["description"])

    # Display available options
    print("Options:")
    for i, option in enumerate(game_map[current_room]["options"], 1):
        print(f"{i}. {option}")

    # Get the player's choice
    choice = input("Enter the number of your choice: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(game_map[current_room]["options"]):
            selected_option = game_map[current_room]["options"][choice - 1]

            # Update the game state based on the selected option
            if current_room == "Entrance":
                if selected_option == "Go inside":
                    current_room = "Cave"
                elif selected_option == "Quit":
                    break
            elif current_room == "Cave":
                if selected_option == "Open chest":
                    current_room = "Treasure Room"
                elif selected_option == "Go back":
                    current_room = "Entrance"
            elif current_room == "Treasure Room":
                if selected_option == "Play again":
                    current_room = "Entrance"
        else:
            print("Invalid choice. Please enter a valid option number.")
    except ValueError:
        print("Invalid input. Please enter a valid option number.")

print("Thank you for playing!")

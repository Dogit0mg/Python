import random

def random_nbr(top_number):
    # Generate a random number between 0 and the maximum number specified by the player
    random_number = random.randint(0, int(top_number))
    return random_number

def start_game():
    # Get the maximum number from the player
    top_number = input("Hello, this is a number guessing game. Type a number to set the maximum range: ")
    random_number = random_nbr(top_number)  # Generate the random number once per round

    while True:
        # Ask the player to guess the number
        player_guess = int(input("Try to guess the number the computer chose: "))  # Convert input to integer
        if player_guess == random_number:
            print("Congratulations, you got it right!")
            break  # Break out of the guessing loop on a correct answer
        else:
            # Inform the player that they guessed wrong
            print("That's not the right number.")

            # Ask if the player wants to try again without revealing the number
            try_again = input("Wanna try again? (yes/no) ")
            if try_again.lower() != "yes":
                print(f"The right number was {random_number}.")  # Reveal the number only if they decide not to play again
                return False  # Return False to indicate that the player does not want to continue

    # Ask if the player wants to start a new game after getting the correct answer
    new_game = input("Do you want to start a new game? (yes/no) ")
    if new_game.lower() == "yes":
        return True  # Return True to indicate that the player wants to start a new game
    else:
        return False  # Return False to indicate that the player does not want to continue

def main():
    while True:  # Main game loop
        if not start_game():  # If the player doesn't want to continue (start_game returns False)
            print("Ok, thanks for playing! Have a nice day!")
            break  # Exit the loop and end the program

# Start the game
main()

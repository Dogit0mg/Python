from turtledemo.penrose import start

print("Welcome, to the quiz!")


def start_game():

    playing = input("Do you wish to start a round? (yes/no) ")
    playing = playing.upper()
    if playing == "YES":
        print("Good luck! ")
    else:
        print("Okay :( ")
        quit()

    # Starts the points variable
    points = 0

    answer = input("1. What does 'CPU' stand for? ").lower()
    if answer == "central processing unit":
        points = points + 1
        print("Correct :) ")
    else:
        print("Incorrect :( 'CPU' stands for 'central processing unit'")

    answer = input("2. What does 'GPU' stand for? ").lower()
    if answer == "graphical processing unit":
        points = points + 1
        print("Correct :) ")
    else:
        print("Incorrect :( 'GPU' stands for 'graphical processing unit'")

    answer = input("3. What's the result of 1+1? ").lower()
    if answer == "2" or answer == "two":
        points = points + 1
        print("Correct :) ")
    else:
        print("Incorrect :( the answer is 2")

    answer = input("4. What's the result of 5+8/2 ").lower()
    if answer == "9" or answer == "nine":
        points = points + 1
        print("Correct :) ")
    else:
        print("Incorrect :( the answer is 9, first we do the division, and then the addition")

    answer = input("5. What's the fifth car with the most sales in the world? ").lower()
    if answer == "corolla" or answer == "corola":
        points = points + 1
        print("Correct :) ")
    else:
        print("Incorrect :( the corolla is the fifth car with the most sales in the world!")

    return points


def main():
    total_points = 5  # Maximum number of points

    while True:
        points = start_game()  # Get the score from start_game
        print(f"You got {points} correct answers out of {total_points} total.")

        # Ask if the player wants to play again
        play_again = input("Do you wish to play again? (yes/no) ").lower()
        if play_again != "yes":
            print("Thanks for playing the game! :)")
            break  # Exit the loop and end the program

main()
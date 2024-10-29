import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND) # Creates the left side of the equation using a random int between 3 and 12
    right = random.randint(MIN_OPERAND, MAX_OPERAND) # Creates the right side of the equation using a random int between 3 and 12
    operator = random.choice(OPERATORS) # Chooses a random operator from the list

    expr = str(left) +" " + operator + " " + str(right) # Creates the expression
    answer = eval(expr) # Stores the right answer

    return expr, answer


wrong = 0
input("Press enter to start! ")
print("--------------------")

start_time = time.time() # Starts the timer

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()

    while True: # If the answer is correct -> break the loop, otherwise -> add 1 to the "wrong" count
        guess = input(f"Problem #{(i + 1)}: {expr} = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time() # Ends the timer
total_time = round(end_time - start_time, 2) # Stores the total time and rounds it to make it easier to read

print("--------------------")
print(f"Nice work !, you finished in {total_time} seconds") # Display the time taken to finish the questions

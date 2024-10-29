import random
from collections import Counter

deposit = int(input("Welcome to the Dreams Come True Slot Machine!. How much would you like to deposit? ")) # Gets the value the player wants to deposit and stores it as an int
dinheiro_total = 0
dinheiro_rodada = 0

slots = ["Morango","Uva","Banana","Diamante","Chocolate","Tesouro","Pizza","Hamburguer"] # The rollable options

while True: # Assigns a random option to each slot, using weights to make the one that are worth more less common to appear
    slot1 = random.choices(slots, [5,5,5,1,5,3,5,5], k=1)[0]
    slot2 = random.choices(slots, [5,5,5,1,5,3,5,5], k=1)[0]
    slot3 = random.choices(slots, [5,5,5,1,5,3,5,5], k=1)[0]
    result = [slot1, slot2, slot3]
    counter = Counter(result)
    duplicates = dict((item,count) for item, count in counter.items() if count > 1) # If there is a duplicate -> store it 

    print(result)
    if duplicates: # If there is a duplicate -> evaluate what duplicate it is and how many times it appeared, adding money accordingly
        for item, count in duplicates.items():
            print(f"You've got lucky!!!, you got '{item}' {count} times!")
            if item == "Diamante" and count == 2:
                dinheiro_rodada = deposit * (10 * count)
                print(f"You won {dinheiro_rodada}$")
            elif item == "Diamante" and count == 3:
                dinheiro_rodada = deposit * (50 * count)
                print(f"You won {dinheiro_rodada}$")
#------------------------------------------------------------------------------------------
            elif item == "Tesouro" and count == 2:
                dinheiro_rodada = deposit * (6 * count)
                print(f"You won {dinheiro_rodada}$")
            elif item == "Tesouro" and count == 3:
                dinheiro_rodada = deposit * (20 * count)
                print(f"You won {dinheiro_rodada}$")
#------------------------------------------------------------------------------------------
            elif item != "Tesouro" or item != "Diamante" and count == 2: # If the item is not a "tesouro" or "diamante" evaluates how many times it appeared and add money accordingly
                dinheiro_rodada = deposit * (2 * count)
                print(f"You won {dinheiro_rodada}$")
            elif item != "Tesouro" or item != "Diamante" and count == 3:
                dinheiro_rodada = deposit * (10 * count)
                print(f"You won {dinheiro_rodada}$")
#------------------------------------------------------------------------------------------
    else: # If there are no duplicates -> sets the money from this round to 0
        dinheiro_rodada = 0
        print("You lost your money :( , but winners don't give up!")
#------------------------------------------------------------------------------------------

    dinheiro_total += dinheiro_rodada - deposit # Creates the total balance from every round played

    print(f"Your total balance is {dinheiro_total}")

    repeat = input("Would you like to spin the wheel again? (yes/no): ").lower()
    if repeat != "yes": # If the player chooses not to spin the wheel again -> ends the loop
        print("You almost hit BIG :(")
        break



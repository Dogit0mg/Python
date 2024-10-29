
mountain_alive = None
steal = None

def mountain(): # Creates a function to be used when the player goes though the mountain and is alive
    if mountain_alive == True:
        print("As you continue on your path, you hear battle noises, two gods are fighting, you're in the middle of it, a projectile hits you, you DIE!")
    else:
        pass

def steall(): # Creates a function to be used when the player chose to steal
    if steal == True:
        print("As you continue on your path, you hear battle noises, two gods are fighting, you're in the middle of it, a projectile hits you, you DIE!")
    else:
        pass

name = input("What's your name? ")
print(f"Welcome {name}, i hope you enjoy this adventure!")

print("Your journey starts in an abandoned church, there is no one inside expect you. There is a golden chest on an altar")
print("You have two options. You can either look inside the chest and take what's there, or, you can leave the church")
player_choice = input("Do you want to leave the church or look inside the chest? (leave/look inside) ") # First choice the player must make

if player_choice.lower() == "leave":
    print("As soon as you leave the church you are surprised by a beautiful view of the nature, the are two paths: You can cross a bridge by the river, or, you can go trough the mountains")
    armour = False # If the player chooses not to look inside the chest sets "armour" to False
elif player_choice.lower() == "look inside":
    print("As you open the chest you see a shiny armour inside, you take the armour and wear it. After equiping yourself, you leave the church")
    armour = True # If the player chooses to look inside the chest sets "armour" to True
    print("As soon as you leave the church you are surprised by a beautiful view of the nature, the are two paths: You can cross a bridge by the river, or, you can go trough the mountains")

player_choice = input("Do you go trough the mountains or across the bridge? (mountains/bridge) ").lower() # Divides the story into 2 different paths
if player_choice == "mountains":
    player_choice = input("As you follow the path you find 5 guys beating and old man, do you intevene or ignore? (intervene/ignore) ").lower()
    if player_choice != "ignore":
        print("You don't know how to fight and don't even have a weapon, you DIE!")
    elif player_choice == "ignore" and armour == True: # Checks to see if the has armour and directs the story accordingly
        print("Your shiny armour draws the attention of the agressors, as you don't know how to fight and have no weapons, you DIE!")
    elif player_choice == "ignore" and armour == False:
        print("You succesfully pass trough them")
        mountain_alive = True # Stores that the player went through the mountains and remained alive and calls for the "mountain" function
        mountain()
elif player_choice == "bridge":
    player_choice = input("As you walk down the path, you find a body, do you search the body and take it's bellongings or do you ignore it? (search/ignore) ").lower()
    if player_choice == "search":
        print("As you search the body, you find and take a gorgeous golden sword ")
        player_choice = input("As soon as you equip it, a thug appears and tries to steal you, do you fight or flee? (fight/flee)")
        if player_choice == "fight" and armour == True: # Decides the result of the battle based on what happened before
            print("Even though you can't fight, you have a good armour and a weapon, you manage to kill the thug and take all his belongings")
            steal = True # Sets the "steal" variable to True and calls the "steall" function
            steall()
        elif player_choice == "fight" and armour == False:
            print("Even though you have a weapon, you can't fight, maybe if you had armour on you it would be possible to win, you DIE!")
        elif player_choice == "flee" and armour == False:
            print("You can't run from him, he catches you and kills you, you DIE!")
        elif player_choice == "flee" and armour == True:
            print("The armour you're wearing makes you slow, the thug catches and kills you, you DIE!")

    elif player_choice == "ignore":
        print("As you walk past the body a thug approaches you and tries to steal you")
        if armour == False:
            print("As you have no armour and no weapon, the thug kills you, you DIE!")
        elif armour == True:
            print("As you only have a piece of armour and no weapon, the thug kills you and steals your armour, you DIE!")


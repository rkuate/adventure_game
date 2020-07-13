import time
import random

# List of potentials ennemies
ennemies = ["pirate", "dragon", "wickie fairie", "troll", "wolf", "witch", "minotaur"]
# Hand of the player ; items he is carrying
hand = ["dagger"]
# Variable name for the sword
sword = "sword"


# Print messages with delays
def print_pause(message):
    print(message)
    # Delay the message by 2 seconds
    time.sleep(0)


# Print the introduction when starting a new game
def intro(ennemy):
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + ennemy +
                " is somewhere around here, and has been"
                " terryfying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not"
                " very effective) dagger.")


# Make sure the player enters valid inputs
# Valid inputs are the choices values
def valid_input(prompt, choices):
    print_pause("\n")
    choice = input(prompt + "\n")
    for item in choices:
        if choice == item:
            return choice
    valid_input(prompt, choices)


# Path when the player decides to knock at the door
def knock_door(ennemy):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps a " + ennemy + ".")
    print_pause("Eep! This is the " + ennemy + "'s house!")
    print_pause("The " + ennemy + " attacks you!")


# Path when the player decides to peer into the cave
def peer_cave():
    print_pause("You peer cautiously into the cave")


# Path when the player peers into the cave without the sword
def peer_cave_dagger(ennemy, ennemies, hand, sword):
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth.")
    print_pause("You discard your silly old dagger and "
                "take the sword with you.")
    print_pause("You walk back out to the field.")
    play_game(ennemy, ennemies, hand, sword)


# Path when the player peers into the cave with the sword
def peer_cave_sword(ennemy, ennemies, hand, sword):
    print_pause("You've been here before, and gotten all the "
                "good stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field.")
    play_game(ennemy, ennemies, hand, sword)


# Path when the player attacks the ennemy with the sword
def sword_attack(ennemy, ennemies, sword):
    print_pause("As the " + ennemy + " moves to attack, "
                "you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your "
                "as you brace yourself for the attack.")
    print_pause("But the " + ennemy + " takes one look at your "
                "shiny new toy and runs away!")
    print_pause("You have rid the town of the " + ennemy + ". "
                "You are victorious!")
    print_pause("\nGAME OVER")
    play_again(ennemies, sword)


# Path when the player attacks the ennemy without the sword
def dagger_attack(ennemy, ennemies, sword):
    print_pause("You do your best...")
    print_pause("but your dagger is no match for the " + ennemy + ".")
    print_pause("You have been defeated!")
    print_pause("\nGAME OVER")
    play_again(ennemies, sword)


# Path when the player decides to run away from the ennemy
def run_away(ennemy, ennemies, hand, sword):
    print_pause("You ran back into the field. Luckily, you "
                "don't seem have been followed.")
    play_game(ennemy, ennemies, hand, sword)


# Request the player to decide whether to restart the game again or not
def play_again(ennemies, sword):
    hand = ["dagger"]
    # Collect the choice for the player
    # Whether to start a new game or exit
    choice_play = valid_input("Would you like to play again? (y/n)",
                              ["y", "n"])
    if (choice_play == "y"):
        print_pause("Excellent! Restarting the game...")
        adventure_game(ennemies, hand, sword)
    elif (choice_play != "n"):
        print_pause("Thanks for playing! See you next time.")
        play_again(ennemies, sword)


# Continue a game ; from the point after the introduction
def play_game(ennemy, ennemies, hand, sword):
    print_pause("Enter 1 to knock at the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    # Collect the choice for the player
    # Whether to knock the door or peer into the cave
    choice_village = valid_input("(Please enter 1 or 2.)",
                                 ["1", "2"])
    if choice_village == "1":
        knock_door(ennemy)
        if sword in hand:
            # Collect the choice for the player
            # Whether to fight or run away
            choice_door = valid_input("Would you like to (1) "
                                      "fight or (2) run away?",
                                      ["1", "2"])
            if choice_door == "1":
                sword_attack(ennemy, ennemies, sword)
            elif choice_door == "2":
                run_away(ennemy, ennemies, hand, sword)
        elif sword not in hand:
            print_pause("You feel a bit under-prepared for this, "
                        "what with only having a tiny dagger.")
            choice_door = valid_input("Would you like to (1) "
                                      "fight or (2) run away?",
                                      ["1", "2"])
            if choice_door == "1":
                dagger_attack(ennemy, ennemies, sword)
            elif choice_door == "2":
                run_away(ennemy, ennemies, hand, sword)
    elif choice_village == "2":
        peer_cave()
        if sword in hand:
            peer_cave_sword(ennemy, ennemies, hand, sword)
        elif sword not in hand:
            # Assign the sword to the player
            hand.append(sword)
            peer_cave_dagger(ennemy, ennemies, hand, sword)


# Main function of the game
def adventure_game(ennemies, hand, sword):
    # Choose randomly a new ennemy each time a new game start
    ennemy = random.choice(ennemies)
    intro(ennemy)
    play_game(ennemy, ennemies, hand, sword)


adventure_game(ennemies, hand, sword)

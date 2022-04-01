import time
import random

# Choose a random weapon
enemy_list = ['DarkVader', 'Bane', 'Thanos', 'GI Jane']
enemy = ''

#initial weapon = dagger
weapon = 'dagger'


# Print and pause info passed as msg
def print_pause(msg):
    print(msg)
    time.sleep(2)


# Choose to play the game again
def play_again():
    choice = get_input("Would you like to play again? (y/n)\n",
                       ['y', 'n'])
    if choice == 'y':
        global weapon
        print_pause("Excellent! Restarting the game...")
        weapon = 'dagger'
        start_game()
    else:
        finish_game()


# Decide method
def decide():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choose_one_or_two()


# Function to make the user choose to
# advance to house or choose a weapon
def choose_one_or_two():
    choice = get_input("Please enter 1 or 2.\n", ['1', '2'])
    if choice == '1':
        advance_to_house()
    else:
        change_weapon()


# When the user choose 1
def advance_to_house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps"
                f" {enemy}.")
    print_pause(f"Eep! This is {enemy}'s house!")
    print_pause(f"{enemy} attacks you!")
    fight_or_run_away()


# Function to fight or run away
def fight_or_run_away():
    choice = get_input("Would you like to (1) fight or (2) run away?\n",
                       ['1', '2'])
    if choice == '1':
        fight()
    else:
        run_away()


# User's choice
def get_input(prompt, values):
    while True:
        choice = input(prompt).lower()
        if choice in values:
            return choice


# Fight the enemy
def fight():
    if weapon == 'sword':
        print_pause(f"As {enemy} moves to attack, you unsheath"
                    f" your new {weapon}.")
        print_pause(f"The {weapon} of Ogoroth shines brightly in your"
                    " hand as you brace yourself for the attack.")
        print_pause(f"But the {enemy} takes one look at your shiny"
                    " new toy and runs away!")
        print_pause(f"You have rid the town of {enemy}"
                    ". You are victorious!")
    else:
        print_pause("You do your best...")
        print_pause(f"But your {weapon} is no match for "
                    f"{enemy}.")
        print_pause("You have been defeated!")
    play_again()


# Run away from the enemy
def run_away():
    print_pause("You run back into the field. Luckily, you don't seem to"
                " have been followed.")
    decide()


# Change the weapon of the user
def change_weapon():
    global weapon
    print_pause("You peer cautiously into the cave.")
    if weapon == 'sword':
        print_pause("You've been here before, and gotten all the"
                    " good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You discard your silly old  {weapon}"
                    " and take the sword with you.")
        weapon = 'sword'
    print_pause("You walk back out to the field.")
    decide()


# Finish the game
def finish_game():
    print("Thanks for playing! See you next time.")


# Print information about the adventure
def start_game():
    global enemy
    enemy = random.choice(enemy_list)
    print_pause("You find yourself standing in an open field, filled" +
                " with grass and yellow widlflowers.")
    print_pause(f"Rumor has it that {enemy} is somewhere around"
                " here, and has been terrifying the nerby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                f"{weapon}.")
    decide()


# Start the adventure game
start_game()

import random

def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are two paths ahead.")
    first_choice()

def first_choice():
    choice = input("Do you want to go left or right? (left/right): ").lower()
    if choice == 'left':
        encounter_creature()
    elif choice == 'right':
        find_treasure()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        first_choice()

def encounter_creature():
    print("You encounter a wild creature!")
    action = input("Do you want to fight or run? (fight/run): ").lower()
    if action == 'fight':
        fight_creature()
    elif action == 'run':
        print("You successfully ran away!")
    else:
        print("Invalid choice. Please choose 'fight' or 'run'.")
        encounter_creature()

def fight_creature():
    if random.choice([True, False]):
        print("You defeated the creature! You win!")
    else:
        print("The creature defeated you. Game over.")

def find_treasure():
    print("You find a hidden treasure chest!")
    print("Congratulations! You win!")

start_game()

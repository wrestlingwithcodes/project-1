from random import randint
import os

dnd_dices = {
        "d4": 4,
        "d6": 6,
        "d8": 8,
        "d10": 10,
        "d12": 12,
        "d20": 20,
        "d100": 100}

def dnd_dice_roller():
    os.system('cls')

    print("Welcome to the D&D Dice Roller!")
    print("You can roll the following type of dices: " + ", ".join(dnd_dices.keys()) + ".")
    while True:
        print("Enter the type of dice you want to roll: ")
        dice_type = input().lower()
        
        if dice_type == "quit".lower() or dice_type == "quit".upper():
            print("Returning to Main Menu...")
            import main_menu            
            main_menu()
        
        elif dice_type not in dnd_dices:
            print("Invalid dice type. Please enter a valid dice type (e.g., " + ", ".join(dnd_dices.keys()) + ").")
            continue
        
        print("Enter the number of dice you want to roll: ")
        num_dice = input()

        if num_dice == "quit".lower() or num_dice == "quit".upper():
            print("Returning to Main Menu...")
            import main_menu
            main_menu()

        elif not num_dice.isdigit() or int(num_dice) <= 0:
            print("Number of dice must be a positive integer.")
            continue

        def dice_roll(dice_type, num_dice):
            dice_sides = int(dice_type[1:])
            rolls = [randint(1, dice_sides) for _ in range(int(num_dice))]
            print(f"You rolled: {rolls}")
        dice_roll(dice_type, num_dice)

        print("Roll again? (y/n)")

        if input().lower() == "n":
            print("Thanks for using the D&D Dice Roller! Returning to Main Menu...")
            import main_menu
            main_menu()
        elif input().lower() == "y":
            dnd_dice_roller()
dnd_dice_roller()
    
# print(list(dnd_dices.values()))
# print(list(dnd_dices.keys()))
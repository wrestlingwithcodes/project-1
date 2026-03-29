import time
from colorama import Fore, Style, Back
import os
def main_menu():
    while True:
        os.system('cls')

        from menu_variables import x1, APP_NAME

        print("╔"+"\\"+APP_NAME+"\\"+"═"*16+"╗")
        print("║                        ║")
        print("║  1 - D&D Dice Roller   ║")
        print("║  2 - Turtle Race       ║")
        print("║  3 - Unit Conversions  ║")
        print("║  4 - Games             ║")
        print("║  5 - Generate Password ║")
        print("║                        ║")
        print("╚"+"<"+x1+"\\"+"═"*14+"╝")

        mainInput = input()

        try:
            if mainInput not in [str(i) for i in range(6)]:
                raise ValueError("Invalid choice. Please enter a number between 0 and 5.")
            if mainInput == "0":
                print("Exiting the program. Goodbye!")
                time.sleep(0.5)
                exit()  
        except ValueError as e:
            print(e)
            main_menu()
        try:

            if mainInput == "1":
                from dnd_dice_roller import dnd_dice_roller
                dnd_dice_roller()
            
            elif mainInput == "2":
                from turtle_race import turtle_race
                turtle_race()

            elif mainInput == "3":
                from converter_menu import converter_menu
                converter_menu()

            elif mainInput == "4":
                from games_menu import games_menu
                games_menu()
            
            elif mainInput == "5":
                from password_generator import password_generator
                password_generator()

            else:
                print(Fore.RED + "Invalid choice. Please enter 0-5." + Style.RESET_ALL)
                time.sleep(1.0)

        except TypeError as e:
            print(e)
            main_menu()
main_menu()
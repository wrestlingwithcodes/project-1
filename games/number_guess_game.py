import random
import time
import os

def guessing_game():
    os.system('cls')
    print("Welcome to the Number Guessing Game!")
    print("Set a guessing range (e.g., 1-100): ")
    print("Type 'quit' at any time to exit the game.")
    user_input = input()    
    try:
        if user_input == "quit".lower() or user_input == "quit".upper():
                print("Returning to main menu...")
                time.sleep(1.5)
                from games_menu import games_menu
                games_menu()

        start_str, end_str = user_input.split('-')
        start = int(start_str)
        end = int(end_str)
        
        print(f"Start of the range: {start}")
        print(f"End of the range: {end}")
    
        print("Numbers in the range:")
        for i in range(start, end + 1):
            print(i)

    except ValueError:
        print("Invalid input. Please enter two valid numbers separated by a hyphen.")
        guessing_game()
    except IndexError:
        print("Invalid format. Please enter the range in the format 'start-end'.")
        guessing_game()

    else:
        number = random.randint(start, end)
        attempts = 0

        while True:
            guess = input(f"Guess a number between {start} and {end}: ")
            if not guess.isdigit():
                print("Please enter a valid number.")
                guessing_game()
            guess = int(guess)
            attempts = attempts + 1
            
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} tries.")
                print("Play again? (y/n)")
                play_again = input().lower()
                if play_again == "y":
                    guessing_game()
                elif play_again == "n":
                    print("Thanks for playing!")
                    print("Returning to games menu...\n")
                    from games_menu import games_menu
                    time.sleep(1.5) 
                    games_menu()
guessing_game()
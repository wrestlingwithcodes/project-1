import time
import random
import colorama
from colorama import Fore, Style, Back
colorama.init()
import os

def word_guess_game():
    os.system('cls')

    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + "Welcome to the Word Guessing Game!" + Style.RESET_ALL)
    print("Type" + Back.BLACK + Fore.RED + " 'quit' " + Style.RESET_ALL + "at any time to exit the game.")
    print("Guess words are in English.")

    def difficulty_select():
        print("Please select a difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        difficulty = input("Enter your choice (1-3): ")

        try:
            if difficulty == "quit".lower() or difficulty == "quit".upper():
                print("Returning to main menu...")
                time.sleep(1.5)
                from games_menu import games_menu
                games_menu()

            elif difficulty not in ["1", "2", "3"]:
                raise ValueError("Invalid choice! Please select a valid difficulty level.")
        
        except ValueError as e:
            print(e)
            return difficulty_select()
        
        return difficulty
    # difficulty_select()
    
    difficulty = difficulty_select()
    # letter_hint_counter = 0

    if difficulty == "1":
        easy_guess_words = ["CAT", "DOG", "FISH", "BIRD",]
        random_word = random.choice(easy_guess_words)
    elif difficulty == "2":
        medium_guess_words = ["PYTHON", "GUITAR", "CRASH" , "RIVER", "FLOWER"]
        random_word = random.choice(medium_guess_words)
    elif difficulty == "3":
        hard_guess_words = ["EXCELLENT","DIFFICULT","MOUNTAIN", "PHILOSOPHER","NUANCE"]
        random_word = random.choice(hard_guess_words)

    def hint_letter():
        if difficulty == "1":
            hint_letter = random.choice(random_word)
            print(f"Hint: The word contains the letter '{hint_letter}'.")
        elif difficulty == "2":
            hint_letter = random.choice(random_word)
            print(f"Hint: The word contains the letter '{hint_letter}'.")
        elif difficulty == "3":
            hint_letter = random.choice(random_word)
            print(f"Hint: The word contains the letter '{hint_letter}'.")
    # hint_letter()

    def give_hint():
        if difficulty == "1":
            print("Hint: The word is an animal.")
        elif difficulty == "2":
            print("Hint: The word is a common noun.")
        elif difficulty == "3":
            print("Hint: The word is a more complex noun.")
     
    print("Guess the word! You have 8 lives. Good luck!")
    guessed_letters = []
    fails = 0
    lives = 8
    while lives > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in random_word])
        print(f"Word: {display_word}")
        print("Lives: " + Style.BRIGHT+Fore.RED + "♥" * lives + Style.RESET_ALL + "♥" * fails) 
        print("Type 'hint' for a hint!")
        print("Type 'letter' for a hint letter! (Costs 3 lives)")
        guess = input("Guess a letter: ").upper()

        try:
            if guess == "quit".lower() or guess == "quit".upper():
                print("Thanks for playing!")
                print("Returning to main menu...")
                from main_menu import main_menu
                time.sleep(1.5)
                games_menu()     

            elif guess == "hint".lower() or guess == "hint".upper():
                give_hint()
                continue

            elif guess == "letter".lower() or guess == "letter".upper():
                lives = lives - 3
                hint_letter()
                continue    
            
            elif guess == "letter".lower() or guess == "letter".upper():
                hint_letter()
                continue

            elif len(guess) != 1 or not guess.isalpha():
                raise ValueError("Please enter a single letter.")
            
            elif guess == "":
                raise ValueError("Input cannot be empty. Please enter a letter.")
            
            elif guess in guessed_letters:
                raise ValueError("You've already guessed that letter. Try a different one.")
            
            else:pass   
            
            

        except ValueError as e:
            print(e)
            continue

        guessed_letters.append(guess)

        if guess in random_word:
            print("Correct!")
            if all(letter in guessed_letters for letter in random_word):
                print(f"Congratulations! You've guessed the word: {random_word}")
                print("Play again? (y/n): ")
                if input().lower() or input().upper() == "y":
                    word_guess_game()
                elif input().lower() or input().upper() == "n":
                    print("Thanks for playing!")
                    print("Returning to main menu...")
                    time.sleep(1.5)
                    from games_menu import games_menu
                    games_menu()
        else:
            print("Wrong!")
            lives = lives - 1
            fails = fails + 1
               
    else:
        print(f"Game Over! The word was: {random_word}")
        print(f"Try again? (y/n): ")
        if input().lower() or input().upper() == "y":
            word_guess_game()
        elif input().lower() or input().upper() or input() == "quit".lower() or input() == "quit".upper() == "n":
            print("Thanks for playing!")
            print("Returning to main menu...")
            time.sleep(1.5)
            from games_menu import games_menu
            games_menu()

word_guess_game()         
    
import time
import os
def games_menu():
    os.system('cls')

    print("╔"+"\\Games\\"+"═"*14+"╗")
    print("║                     ║")
    print("║  1 - Number Guesser ║")
    print("║  2 - Word Guesser   ║")
    print("║  3 - Tic-Tac-Toe    ║")
    print("║                     ║")
    print("╚"+"<0 - Return\\"+"═"*9+"╝")

    choice = input()

    try:
        if choice not in [str(i) for i in range(5)]:
            raise ValueError("Invalid choice. Please enter a number between 0 and 5.")
        if choice == "0":
            print("Returning to main menu...")
            time.sleep(0.5)
            from main_menu import main_menu
            main_menu()
    except ValueError as e:
        print(e)
        games_menu()
    
    if choice == "1":
        from games.number_guess_game import guessing_game
        guessing_game()

    elif choice == "2":
        from games.word_guess_game import word_guess_game
        word_guess_game()

    elif choice == "3":
        from games.tictactoe_game import tictactoe_game
        tictactoe_game()
        
    elif choice in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print("This game is coming soon! Please check back later.")
        games_menu()
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")
        games_menu()
games_menu()
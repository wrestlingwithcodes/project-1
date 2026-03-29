import time
import os
def tictactoe_game():
    os.system('cls')

    print("Welcome to Tic Tac Toe!")
    print("This is a two-player game. Player 1 is 'X' and Player 2 is 'O'.")
    print("Type 'quit' at any time to exit the game.")

    def print_board(board):
        for row in range(0, 9, 3):
            print(f"{board[row]} | {board[row+1]} | {board[row+2]}")
            if row < 6:
                print("--+---+--")

    def check_winner(board):
        win_cond = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in win_cond:
            if board[a] == board[b] == board[c] and board[a] != " ":
                return board[a]
        return None

    def play_game():
        board = [" "] * 9
        current_player = "X"
        
        print("\nNew Game Started")
        print("Type 'quit' at any time to exit.\n")

        for turn in range(9):
            print_board(board)
            user_input = input(f"Player {current_player}, choose a spot (1-9) or 'quit': ").lower().strip()

            if user_input == 'quit':
                print("Returning to Games Menu...")
                from games_menu import games_menu
                time.sleep(0.75)
                games_menu()

            try:
                move = int(user_input) - 1
                if move < 0 or move > 8:
                    print("Please enter a number between 1 and 9.")
                    continue
                if board[move] != " ":
                    print("Spot taken! Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter 1-9 or 'quit'.")
                continue

            board[move] = current_player
            winner = check_winner(board)
            
            if winner:
                print_board(board)
                print(f"Congrats! Player {winner} wins!")
                game_end_choice = input(f'Play again? (y/n)')
                if game_end_choice == "y":
                    play_game()
                elif game_end_choice == "n":
                    from games_menu import games_menu
                    games_menu()

                return

            current_player = "O" if current_player == "X" else "X"

        print_board(board)
        print("It's a draw!")
        draw_choice = input(f"Play again? (y/n)")
        if draw_choice == "y":
            play_game()
        elif draw_choice == "n":
            from games_menu import games_menu
            games_menu()
    play_game()
tictactoe_game()
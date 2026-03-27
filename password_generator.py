import random
import string
import os
import time

def password_generator():
    
    while True:
        os.system('cls')
        print("Welcome to Password Generator.")
        print("Generate a strong password.")
        print("Type 'quit' to return to Main Menu.")

        length_input = input("\nEnter desired password length.\nPasswords should be at least 4 characters for security.: ").strip().lower()

        if length_input == 'quit':
            import main_menu
            main_menu()

        try:
            length = int(length_input)
            
            if length < 4:
                print("Password should be at least 4 characters for security!")
                time.sleep(0.75)
                continue

            characters = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.choice(characters) for i in range(length))

            print(f"Your Password: {password}")
            input("\nPress Enter to generate another or type 'quit'...")

        except ValueError:
            print("Invalid input! Please enter a number or 'quit'.")
password_generator()
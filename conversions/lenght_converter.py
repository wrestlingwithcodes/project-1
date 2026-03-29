import os

def length_converter():
    while True:
        os.system('cls')
        print("Welcome to Length Converter.")
        print("1. Inches to Centimeters (cm)")
        print("2. Centimeters (cm) to Inches")
        print("\nType 'quit' to go back.")

        choice = input("\nSelect (1-2): ").lower()
        if choice == 'quit':
            from converter_menu import converter_menu
            converter_menu()

        try:
            val = input("Enter length value (or 'quit'): ").lower()
            if val == 'quit': return
            length = float(val)

            if choice == "1":
                res = length * 2.54
                print(f"\n {length} inches = {res:.2f} cm")
            elif choice == "2":
                res = length / 2.54
                print(f"\n {length} cm = {res:.2f} inches")

            input("\nPress Enter to continue.")
        
        except ValueError:
            print("Invalid number!")
length_converter()
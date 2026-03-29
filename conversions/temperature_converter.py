import os

def temperature_converter():
    while True:
        os.system('cls')
        print("Welcome to Temperature Converter.")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("\nType 'quit' to go back.")

        choice = input("\nSelect (1-2): ").strip().lower()
        if choice == "quit":
            from converter_menu import converter_menu
            converter_menu()

        try:
            val = input().strip().lower()
            if val == 'quit': return
            temp = float(val)

            if choice == "1":
                res = (temp * 9/5) + 32
                print(f"\n{temp}°C = {res:.2f}°F")
            elif choice == "2":
                res = (temp - 32) * 5/9
                print(f"\n{temp}°F = {res:.2f}°C")
            
            input("\nPress Enter to continue...")
        except ValueError:
            print("Invalid number!")
temperature_converter()
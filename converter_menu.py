import os
import time

def converter_menu():
    os.system('cls')

    print("╔"+"\\Conversions\\"+"═"*17+"╗")
    print("║                              ║")
    print("║  1 - Time Zone Conversion    ║")
    print("║  2 - Temperature Conversion  ║")
    print("║  3 - Measurement Conversion  ║")
    print("║                              ║")
    print("╚"+"<0 - Return\\"+"═"*18+"╝")

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
        converter_menu()
    if choice == "1":
        from conversions.tz_converter import time_converter
        time_converter()
    elif choice == "2":
        from conversions.temperature_converter import temperature_converter
        result = temperature_converter()
        if result == 'BACK_TO_MAIN':
            return
    elif choice == "3":
        from conversions.lenght_converter import length_converter
        length_converter()
converter_menu()
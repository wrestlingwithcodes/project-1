import pytz
from datetime import datetime
import os

def time_converter():
    zones = {
        "1": ("Turkey", "Europe/Istanbul"),
        "2": ("England", "Europe/London"),
        "3": ("US/West", "America/Los_Angeles"),
        "4": ("US/East", "America/New_York"),
        "5": ("Russia", "Europe/Moscow"),
        "6": ("China", "Asia/Shanghai")
    }

    while True:
        os.system('cls')
        print("Welcome to Time Zone Converter.")
        for key, (name, _) in zones.items():
            print(f"{key}. {name}")
        print("\nType 'quit' to go back to Unit Converter Menu.")

        choice = input("\nSelect source (1-6): ").strip().lower()
        
        if choice == 'quit':
            import converter_menu
            converter_menu()

        target_choice = input("Select target (1-6): ").strip().lower()
        
        if target_choice == 'quit':
            import converter_menu
            converter_menu()

        if choice in zones and target_choice in zones:
            src_name, src_db = zones[choice]
            tgt_name, tgt_db = zones[target_choice]

            try:
                source_tz = pytz.timezone(src_db)
                target_tz = pytz.timezone(tgt_db)
                
                now = datetime.now(source_tz)
                target_now = now.astimezone(target_tz)

                print("\n" + "="*35)
                print(f"{src_name:10} | {now.strftime('%H:%M:%S')}")
                print(f"{tgt_name:10} | {target_now.strftime('%H:%M:%S')}")
                print("="*35)
                
                input("\nPress Enter to continue or type 'quit'...")
            except Exception as e:
                print(f"Error: {e}")
                input("Press Enter to try again...")
        else:
            print("Invalid selection! Please use numbers 1-6 or type 'quit'.")
            input("Press Enter to try again...")
time_converter()
import turtle
import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init
import os

def turtle_race():
    os.system('cls')

    print("Welcome to Turtle Racing!")
    # turtle_racers = {"Flash" :  "red", 
    #                   "Speedy" :  "blue", 
    #                  "Lightning" : "yellow", 
    #                   "Turbo" :  "green" }
    turtle_racers = {Fore.RED + "Flash" + Style.RESET_ALL:  "red", 
                     Fore.BLUE + "Speedy" + Style.RESET_ALL:  "blue", 
                     Fore.YELLOW + "Lightning" + Style.RESET_ALL: "yellow", 
                     Fore.GREEN + "Turbo" + Style.RESET_ALL:  "green" }

    winner = ""
    # print(winner)
    # print(type(winner))
    while True:

        print("The racers are:")
        for i in range(len(turtle_racers)):
            print(str(i + 1) + ". " + list(turtle_racers.keys())[i])
        
        bet = int(input(f"Enter the number of the turtle you want to bet on (1-{len(turtle_racers)}): "))
        # print(bet)
        # print(type(bet))
        
        if bet == 1:
            winner = Fore.RED + "Flash" + Style.RESET_ALL
        elif bet == 2:
            winner = Fore.BLUE + "Speedy" + Style.RESET_ALL
        elif bet == 3:
            winner == Fore.YELLOW + "Lightning" + Style.RESET_ALL
        elif bet == 4:
            winner = Fore.GREEN + "Turbo" + Style.RESET_ALL

        # print(winner)
        # print(type(winner))
        
        try:
            if bet not in range(1, len(turtle_racers) + 1):
                raise ValueError("Invalid bet. Please choose a valid turtle number.")

            elif bet == "":
                raise TypeError("Invalid bet. Please choose a valid turtle number.")
                   
        except ValueError:
            print("Invalid bet. Please choose a valid turtle number.")
            continue  
        
        else:
            print("The race is about to start!")
            time.sleep(0.5)

            screen = turtle.Screen()
            screen.title("Turtle Racing")
            screen.bgcolor("lightgreen")

            finish_line = 200
            line = turtle.Turtle()
            line.hideturtle()
            line.penup()
            line.goto(finish_line,-200)
            line.left(90)
            line.pendown()
            line.pensize(3)
            line.color("black")
            line.forward(400)

            turtles = []
            
            for name, colour in turtle_racers.items():
                racer = turtle.Turtle()
                racer.color(colour)
                racer.shape("turtle")
                racer.penup()
                racer.goto(-200, (len(turtles) - 2) * 40)
                turtles.append((name, racer))


            while True:
                for name, racer in turtles:
                    racer.forward(random.randint(1, 10))
                    if racer.xcor() >= finish_line:
                        print(f"{name} wins the race!")
                        # print(name)
                        # print(type(name))
                        # print(winner)
                        # print(type(winner))

                        if winner == name:
                            print("Congratulations! You won your bet!")
                            screen.exitonclick()
                            play_again = input("Play again?(y/n)")
                            if play_again == "y":
                                turtle_race()
                            elif play_again == "n":
                                import main_menu
                                main_menu()
                            
                        else:                    
                            print("Sorry, you lost your bet. Better luck next time!")
                            screen.exitonclick()
                            play_again = input("Play again?(y/n)")
                            if play_again == "y":
                                turtle_race()
                            elif play_again == "n":
                                import main_menu
                                main_menu()
                        time.sleep(1.0)
                        screen.exitonclick()
turtle_race()

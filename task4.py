import time

def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest with two paths ahead.")
    print("Your choices will determine your fate. Choose wisely!\n")

def make_choice(choices):
    print("Choose your action:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            user_input = int(input("Enter the number of your choice: "))
            if 1 <= user_input <= len(choices):
                return user_input
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def forest_path():
    print("You take the left path and come across a river.")
    time.sleep(1)
    print("What do you do?")
    
    choices = ["Cross the river on a shaky bridge.", "Swim across the river."]
    user_choice = make_choice(choices)

    if user_choice == 1:
        print("The bridge collapses, and you fall into the river. Game over!")
    elif user_choice == 2:
        print("You swim across safely and find a treasure chest. Congratulations, you win!")

def cave_path():
    print("You take the right path and enter a dark cave.")
    time.sleep(1)
    print("You see two tunnels. Which one do you choose?")

    choices = ["Go left.", "Go right."]
    user_choice = make_choice(choices)

    if user_choice == 1:
        print("You encounter a friendly dragon. It leads you to an exit. Congratulations, you win!")
    elif user_choice == 2:
        print("You get lost in the cave. Game over!")

def main():
    intro()
    time.sleep(1)
    print("You can choose between two paths.")
    
    choices = ["Take the left path.", "Take the right path."]
    user_choice = make_choice(choices)

    if user_choice == 1:
        forest_path()
    elif user_choice == 2:
        cave_path()

if __name__ == "__main__":
    main()

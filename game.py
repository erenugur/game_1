import time

def intro():
    name = input("Hello user. Enter your name: ")
    print(f"Greetings, {name}. Your journey starts now.")

def journey():
    print("You are stranded in a jungle. What do you do?")
    time.sleep(2)
    print("A: Call for help.")
    time.sleep(1)
    print("B: Walk north for ten minutes.")
    time.sleep(1)
    print("C: Walk south for ten minutes.")
    time.sleep(1)
    print("D: Do nothing.")
    time.sleep(1)
    choice1 = input("Enter here: ")

    while True:
        if choice1 == "A":
            print("Nobody comes for help, but a bush near you rattles.")
            break
        elif choice1 == "B":
            print("You come across a native tribe that lives in huts. Do you enter the tribe?")
            break
        elif choice1 == "C": 
            print("You arrive at the coast of the jungle, and you gaze upon the ocean. Do you walk left or right of the ocean?")
            break
        elif choice1 == "D": 
            print("A pack of gorillas find and eat you. Game over!")
            break
        else:
            choice1 = input("Please enter A, B, C, or D: ")

def game():
    intro()
    time.sleep(2)
    journey()


game()

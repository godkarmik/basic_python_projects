import random
import time

choice = ''
result = ''
def welcome():
    print("WELCOME TO ROCK PAPER SCISSORS GAME !")

def user_input():
    global choice
    choice = str(input("Enter rock , paper or scissors / press q to quit: "))
    choice = choice.lower()
    if choice == "q":
        exit()
    print( f"You choose : {choice}")




def computer_choice():
    global result
    v1 = "rock"
    v2 = "paper"
    v3 = "scissors"
    random_choice = random.randint(0,2)
    print("COMPUTER IS CHOOSING : PLEASE WAIT!")
    time.sleep(3)
    if random_choice == 0 :
        result = v1
        print("computer choose : " + result)
    elif random_choice == 1 :
        result = v2
        print("computer choose : " + result)
    else :
        result = v3
        print("computer choose : " + result)

def main():
    if result == choice :
        print("IT IS A TIE!")

    elif (result == "rock" and choice == "paper") or (result == "paper" and choice == "scissors") or (result == "scissors" and choice == "rock") :
        print("YOU won!")

    elif (result == "paper" and choice == "rock") or (result == "scissors" and choice == "paper") or (result == "rock" and choice =="scissors") :
        print("YOU lost!")
    else :
        print("INCORRECT CHOICE ")



while (choice != "q"):
    welcome()
    user_input()
    computer_choice()
    main()
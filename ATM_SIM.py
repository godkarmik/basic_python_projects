import time

atm_on = True
def welcome():
    name= input("Enter your name: ")
    print("[+]welcome " + name + " to karmik ATM")
    print("[+]initializing your ATM Bank")
    time.sleep(3)


def pin_setup():
    global atm_on
    if atm_on == True:
        user_pin = 1234
        input_pin = int(input("enter your ATM PIN :"))
        print("Please wait while we check your pin")
        time.sleep(3)
        if input_pin != user_pin:
             print("[+] Your pin does not match !")
             exit()

def main_opertaion():
     global atm_on
     balance = 1000
     while atm_on == True :

         print("""[+] MAIN MENU : 
    [1]CHECK BALANCE : 
    [2]DEPOSITE MONEY:  
    [3]WITHDRAW MONEY: 
    [4]EXIT: """)
         data = int(input('Enter your choice : '))
         if data == 1 :
             print("BALANCE : " +  str(balance)+ "\n" )
             time.sleep(3)
         elif data == 2 :
             deposite_money = int(input("Enter deposite amount: "))
             balance = balance + deposite_money
             time.sleep(3)
             print("[+]Deposite amount successfull \n")
             time.sleep(2)
         elif data == 3 :
             withdraw_money = int(input("Enter withdrawl amount : "))
             if balance < withdraw_money :
                 print("INSUFFICIENT BALANCE ! \n")
             else :
                 print("[+]Withdrawing money please wait ")
                 time.sleep(5)
                 balance = balance - withdraw_money
                 print("MONEY WITHDRAWN SUCCESSFULLY ! "
                       "BALANCE LEFT : " + str(balance) + "\n")
                 time.sleep(2)
         elif data == 4 :
             print("EXITING GOODBYE!")
             atm_on = False
             exit()
         else :
             print("incorrect value !")




welcome()
pin_setup()
main_opertaion()


#number guessing game 

import time 
import random


def rules ():
    print("                    A random number from 1 to 100 will be chosen                      ")
    print("You will win the game if either you guess the correct number or you ran out of choices")

def level():
    print("This game will have 4 level of difficulty")
    print("1. Easy      (10 chaces with hints)")
    print("2. Medium    (5 chances will hints)")
    print("3. Hard      (3 chances with hints)")
    print("4. grounded  (3 chances with no hints)")
    

def level_1():
    is_running = True
    chances = 0 
    computer_choice = random.randint (1,100) 
    while is_running  :
        human_choice = input("enter your choice btw the range 1 to 100: ")
        if human_choice.isdigit() :
            human_choice = int(human_choice)
            if human_choice in range (1,101):
                chances = chances +1
                if human_choice == computer_choice:
                   print("perfect")
                   is_running = False 
                elif human_choice > computer_choice :
                    print("*************************************")
                    print("   guess a smaller number next time  ")
                    print("*************************************")
                    print(f"you have {10 - chances} chances left")
                    print("*************************************")
                elif chances == 10 :
                    is_running = False
                    print ("oops you ran out of chances")
                else:
                    human_choice < computer_choice 
                    print("*************************************")
                    print("guess a bit larger number next time")
                    print("*************************************")
                    print(f"you have {10 - chances} chances left")
                    print("*************************************")
                
            else :
                print ("enter the value in the given range")
                
        else:
            print("enter a numerical value")

def level_2():
    is_running = True
    chances = 0 
    computer_choice = random.randint (1,100) 
    while is_running  :
        human_choice = input("enter your choice btw the range 1 to 100: ")
        if human_choice.isdigit() :
            human_choice = int(human_choice)
            if human_choice in range (1,101):
                chances = chances +1
                if human_choice == computer_choice:
                   print("perfect")
                   is_running = False 
                elif human_choice > computer_choice :
                    print("*************************************")
                    print ("guess a smaller number next time ")
                    print("*************************************")
                    print(f"you have {5 - chances} chances left")
                    print("*************************************")
                elif chances == 5 :
                    is_running = False
                    print ("oops you ran out of chances")
                else:
                    human_choice < computer_choice 
                    print("*************************************")
                    print("guess a bit larger number next time")
                    print("*************************************")
                    print(f"you have {5 - chances} chances left")
                    print("*************************************")
                
            else :
                print ("enter the value in the given range")
                
        else:
            print("enter a numerical value")

def level_3():
    is_running = True
    chances = 0 
    computer_choice = random.randint (1,100) 
    while is_running  :
        human_choice = input("enter your choice btw the range 1 to 100: ")
        if human_choice.isdigit() :
            human_choice = int(human_choice)
            if human_choice in range (1,101):
                chances = chances +1
                if human_choice == computer_choice:
                   print("perfect")
                   is_running = False 
                elif human_choice > computer_choice :
                    print("*************************************")
                    print ("guess a smaller number next time ")
                    print("*************************************")
                    print(f"you have {3 - chances} chances left")
                    print("*************************************")
                elif chances == 3 :
                    is_running = False
                    print ("oops you ran out of chances")
                else:
                    human_choice < computer_choice 
                    print("*************************************")
                    print("guess a bit larger number next time")
                    print("*************************************")
                    print(f"you have {3 - chances} chances left")
                    print("*************************************")
                
            else :
                print ("enter the value in the given range")
                
        else:
            print("enter a numerical value")

def level_4():
    is_running = True
    chances = 0 
    computer_choice = random.randint (1,100) 
    while is_running  :
        human_choice = input("enter your choice btw the range 1 to 100: ")
        if human_choice.isdigit() :
            human_choice = int(human_choice)
            if human_choice in range (1,101):
                chances = chances +1
                if human_choice == computer_choice:
                   print("perfect")
                   is_running = False 
                elif chances == 3 :
                    is_running = False
                    print ("oops you ran out of chances")
                    
                else:
                    print("*************************************")
                    print("wrong guess try again")
                    print("*************************************")
                    print(f"you have {3 - chances} chances left")
                    print("*************************************") 
                
                
            else :
                print ("enter the value in the given range")
                
        else:
            print("enter a numerical value")


def main():
    is_running = True
    print("*****************************************************************************************************")
    print("**********************         welcome to the number guessing game         **************************")
    print("*****************************************************************************************************")
    rules()
    print("*****************************************************************************************************")
    print("*****************************************************************************************************")
    level()
    human_level_choice = input ("Enter a level at which you want to play(1/2/3/4): ")
    if human_level_choice.isdigit():
        human_level_choice = int(human_level_choice)
        while human_level_choice in range(1,5):
            if human_level_choice == 1:
                level_1()
                break

            elif human_level_choice == 2:
                level_2()
                break

            elif human_level_choice == 3:
                level_3()
                break

            else :
                human_level_choice == 4 
                level_4()
                break
            
    

        else:
            return print ("not a valid option") 
    else:
        print("pls numerical value")
    print("*****************************************************************************************************")
    print("*****************************************************************************************************")
    print("                           THANK FOR PLAY THE NUMBER GUESSING GAME                                   ")
    print("*****************************************************************************************************")
    print("*****************************************************************************************************")
    

if __name__ == "__main__":
    main()
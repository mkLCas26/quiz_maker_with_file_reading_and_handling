# Main Quiz App Program

# import libraries and code files
import os
import time
from pyfiglet import Figlet
from sample_quiz import run_prequiz, sample_ques
from user_quiz import input_user_quiz

# function for clearing screen 
def clear_content():
    os.system('cls' if os.name == "nt" else "clear")

# Inserts ASCII art for title
test = Figlet(font='elite')
clear_content()
print(test.renderText('~ Quiz Master ~'))
time.sleep(1)

# enter username
username = input("\n\nHi! Enter your username: ")
clear_content()

# Loop for the controls
while True: 
    clear_content()
    print(test.renderText('~ Quiz Master ~'))
    print(f"\n\nWelcome to Quiz Master, {username}")
    print(f"What would you like to do?")
    print(f"   [1] Create Quiz (10 Questions)")
    print(f"   [2] Take Sample Quiz (Random 5 Items Science Quiz)")
    print(f"   [3] Answer Your Created Quiz")
    print(f"   [4] Exit")
    
    selected = input("Select an option (1-4): ")
    
    if selected == "1":
        clear_content()
        print(test.renderText('~ Quiz Master ~'))
        input_user_quiz()
        input("\n\nPress Enter to return to Main Menu")
        clear_content()
    
    elif selected == "2":
        clear_content()
        print(test.renderText('~ Quiz Master ~'))
        run_prequiz(sample_ques)
        input("\n\nPress Enter to return to Main Menu")
        clear_content()
        
    elif selected == "3":
        clear_content()
        print(test.renderText('~ Quiz Master ~'))
        print("\n\nThis feature will be revealed soon...!")
        input("\n\nPress Enter to return to Main Menu")
        clear_content()
    
    elif selected == "4":
        print(f"\n\nAww! Thank you for playing, see you soon {username}!")
        break
    
    else:
        print("Invalid! Only select from 1-4. Kindly try again.")
        time.sleep(0.5)
        clear_content()
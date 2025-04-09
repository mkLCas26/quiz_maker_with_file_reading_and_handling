# Main Quiz App Program

# import libraries and code files
import os
import time
from pyfiglet import Figlet
from sample_quiz import run_prequiz
from user_quiz import input_user_quiz

# clearing screen
def clear_content():
    os.system('cls' if os.name == "nt" else "clear")

# Inserts ASCII art for title
test = Figlet(font='elite')
print(test.renderText('~ Quiz Master ~'))
time.sleep(1.5)

# Ask for username
username = input("\n\nHi! Enter your username: ")
clear_content()

# Loop for the controls
while True: 
    print(test.renderText('~ Quiz Master ~'))
    time.sleep(1)
    print(f"\n\nWelcome to Quiz Master, {username}")
    print(f"What would you like to do?")
    print(f"   [1] Create Quiz (10 Questions)")
    print(f"   [2] Take Sample Quiz (Random 5 Items Science Quiz)")
    print(f"   [3] Exit")
    
    selected = input("Select an option (1-3): ")
    
    if selected == "1":
        clear_content()
        input_user_quiz()
        print("\n\nPress Enter to return to Main Menu")
        clear_content()
    
    elif selected == "2":
        clear_content()
        run_prequiz()
        print("\n\nPress Enter to return to Main Menu")
        clear_content()
        
    elif selected == "3":
        print(f"\n\nAww! Thank you for playing, see you soon {username}!")
        break
    
    else:
        print("Invalid! Only select from 1-4. Kindly try again.")
        time.sleep(0.5)
        clear_content()



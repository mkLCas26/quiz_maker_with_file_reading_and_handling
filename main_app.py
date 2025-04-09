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



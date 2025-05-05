# For Answering User Input Quiz

# import libraries
import os
import random

# function that allows user to choose a quiz file from folder
def list_avail_quizzes():
    quizzes = []
    
    # checks if result_folder contains quiz files
    for file in os.listdir("result_folder"):
        if file.endswith(".txt"):
            quizzes.append(file)
    
    if not quizzes:
        print("\nThere's no quizzes created yet.")
        return None
    
    
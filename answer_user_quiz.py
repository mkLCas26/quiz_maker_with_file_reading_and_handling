# For Answering User Input Quiz

# import libraries
import os
import random

# function that allows user to choose a quiz file from folder
def list_avail_quizzes():
    quizzes = []
    
    # checks if result_folder contains quiz files
    for file in os.listdir("result_folder"):
        if file.endswith(".txt") and file != "!ReadMe.txt":
            quizzes.append(file)
    
    if not quizzes:
        print("\nThere's no quizzes created yet.")
        return None
    
    # giving user a printed list of quiz files
    print("\nSaved Quiz Files:")
    for count in range(len(quizzes)):
        print(f"[{count + 1}] {quizzes[count]}")
     
    # allows user to select quiz file   
    while True:
        try:
            select = int(input("\nEnter the assigned number of the quiz you want to take: "))
            
            if 1 <= select <= len(quizzes):
                return os.path.join("result_folder", quizzes[select - 1])
            else:
                print("Invalid. Try Again.")
                
        except ValueError:
            print("Only enter numbers. Try Again.")
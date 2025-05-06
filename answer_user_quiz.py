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

# function that loads/readies selected quiz file for answering     
def load_selected_quiz(quiz_file):
    questions = []
    with open(quiz_file, "r") as file:                                       # opens and reads quiz file selected
        lines = file.readlines()
    
    questions = []
    index = 0
    
    while index < len(lines):                                                # main loop for reading file lines
        start_line = lines[index].strip()
        
        if start_line.startswith("Question: "):                              # extracts the question prompt
            prompt = start_line[len("Question: "):].strip()
            
            choices = []                                                     # for loop for extracting choices and storing it in a list
            for _ in range(4):
                choices_line = lines[index].strip()
                choices.append(choices_line)
                index += 1
            
            answer_line = lines[index].strip()                               # extracts the correct answer
            correct = answer_line[("Correct Answer: "):].strip()
            index += 1
            
            questions.append((prompt, choices, correct))                     # stores all the question into 1 list
        
        index += 1
    return questions  
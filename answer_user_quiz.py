# For Answering User Input Quiz

# import libraries
import os
import random

# function that allows user to choose a quiz file from folder
def list_avail_quizzes():
    quizzes = []
    
    # checks if result_folder contains quiz files
    for file in os.listdir("result_folder"):
        if file.endswith(".txt") and (file != "!ReadMe.txt") and "sample-quiz" not in file:
            quizzes.append(file)
        # elif (file == "!ReadMe.txt") and file.find("sample-quiz"):
        #     quizzes.remove(file)
             
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
    with open(quiz_file, "r") as file:                                  # opens and reads quiz file selected
        lines = file.readlines()
    
    questions = []
    index = 0
    
    while index < len(lines):                                           # main loop for reading file lines
        start_line = lines[index].strip()
        
        if start_line.startswith("Question: "):                         # extracts the question prompt
            prompt = start_line[len("Question: "):].strip()
            
            choices = []                                                # for loop for extracting choices and storing it in a list
            for _ in range(4):
                choices_line = lines[index].strip()
                choices.append(choices_line)
                index += 1
            
            answer_line = lines[index].strip()                          # extracts the correct answer
            correct = answer_line[("Correct Answer: "):].strip()
            index += 1
            
            questions.append((prompt, choices, correct))                # stores all the question into 1 list
        
        index += 1
    return questions

# function that makes the user answer their selected quiz
def answer_selected_quiz():
    quiz_file = list_avail_quizzes()                                    # gets the filepath of selected quiz
    if quiz_file is None:
        return
    
    print(f"\nLoading your selected quiz: {quiz_file}")                 # shuffles the 10 quetions of user
    questions = load_selected_quiz(quiz_file)
    random.shuffle(questions)
      
    score = 0
    quiz_history = []
    correct_letter = ""
    username = input("\nEnter your username again: ")
    print("\n--------------------\n")
    
    for number, item in enumerate(questions, 1):                             
        prompt = item[0]                                                # ensures the correct order of prompt, choices, and answer
        choices = item[1]
        correct_ans = item[2]
        
        print(f"Question {number}: {prompt}")                           # loop to print questions and choices
        for letter, choice in enumerate(choices):
            print(f"{    chr(65 + letter)}. {choice}")
            
        user_answer = (input(f"\nAnswer (A-D): ")).upper()              # checking of user's answer
        if ord(user_answer[0]) - 65 == item.correct:
            score += 1
            print("Correct!\n")
        else:
            correct_letter = chr(65 + correct_ans )
            print(f"Incorrect. The correct answer is {correct_letter}. {choice[correct_ans]}\n")
        
        quiz_history.append({                                                # appends user's quiz history in a list
            "question": prompt,
            "choices": choices,
            "answer": user_answer,
            "correct_choice": f"{correct_letter}. {choice[correct_ans]}"  
        })

    print("--------------------")
    print(f"Congratulations! You have scored {score} out of 10 questions.")  
    
    # Save user's results in a file
    result_files = "result_folder"
    os.makedirs(result_files, exist_ok=True)
    
    # Prepare username for filename
    format_username = username.replace(" ", "_").lower()
    user_filename = f"{format_username}_result"
    count_files = os.listdir(result_files)
    
    # Adds trial number in filename
    trial = 1
    while (f"{user_filename}_try{trial}.txt") in count_files:
        trial +=1
    
    final_filename = f"{user_filename}_try{trial}.txt"
    file_path = os.path.join(result_files, final_filename)
    quiz_title = os.path.basename(quiz_file)                           # extracts quiz title
    
    # Save user's quiz history in file
    with open(file_path, "w") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Quiz Taken: {quiz_title}\n")
    
    
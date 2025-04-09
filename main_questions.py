# Main Quiz Logic (for pre-programmed 5 item quiz)

# import libraries
import random
import os
import re 

# class for quiz questions
class SampleQuestions:
    def __init__(self, prompt, choices, correct):
        self.prompt = prompt
        self.choices = choices
        self.correct = correct

# list of question prompts
question_prompts = [
    "What is the largest ocean in the world?",
    "What is the deepest trench in the world?",
    "What is largest gas planet?",
    "How much of the Earth's surface is water mass?",
    "What is the second most abundant element in the Earth's atmosphere?",
    "What is Earth's highest point above sea level?",
    "How old is Earth?",
    "What plate is the fastest-moving among all of Earth's plates?",
    "What planet has the most moons/satelites?",
    "What are the Earth's four major layers?"
]

# list of questions with choices and correct answer index
sample_ques = [
    SampleQuestions(
        question_prompts[0],
        ["Pacific Ocean", "Indian Ocean", "Arctic Ocean", "Atlantic Ocean"],
        0
    ),
    
    SampleQuestions(
        question_prompts[1],
        ["Kermadec Trench", "Tonga Trench", "Marianas Trench", "New Britain Trench"],
        2
    ),
    
    SampleQuestions(
        question_prompts[2],
        ["Saturn", "Neptune", "Uranus", "Jupiter"],
        3
    ),
    
    SampleQuestions(
        question_prompts[3],
        ["70%", "71%", "68%", "73%"],
        1
    ),
    
    SampleQuestions(
        question_prompts[4],
        ["Nitrogen", "Argon", "Carbon Dioxide", "Oxygen"],
        3
    ),
    
    SampleQuestions(
        question_prompts[5],
        ["Kangchenjunga", "Mount Ararat", "K2", "Mount Everest"],
        3
    ),
    
    SampleQuestions(
        question_prompts[6],
        ["About 4.54 billion years", "About 5 billion years", "About 4.6 billion years", "About 8.1 billion years"],
        0
    ),
    
    SampleQuestions(
        question_prompts[7],
        ["South American Plate", "North American Plate", "Pacific Plate", "African Plate"],
        2
    ),
    
    SampleQuestions(
        question_prompts[8],
        ["Earth", "Saturn", "Jupiter", "Uranus"],
        1
    ),
    
    SampleQuestions(
        question_prompts[9],
        ["Shell, Mantle, First Core, Second Core", "Crust, Mantle, Outer Core, Inner Core",
         "Cover, Mantle, Inner Core, Outer Core", "Crust, Second Layer, Contents, Specifics"],
        1
    )
]

def run_prequiz(sample_ques):
    score = 0 
    quiz_history = []
    username = input("Enter your username: ")
    print("\n--------------------\n")
    
    selected_questions = random.sample(sample_ques, 5)            # for random  5 questions/10
 
    for number, item in enumerate(selected_questions, 1):         # for printing questions and choices
        print(f"Question {number}: {item.prompt}")
        for letter, choice in enumerate(item.choices):
            print(f"{chr(65 + letter)}. {choice}")
            
        user_answer = (input(f"\nAnswer (A-D): ")).upper()
        if ord(user_answer[0]) - 65 == item.correct:              # for checking user answer
            score += 1
            print("Correct!\n")
        else:
            correct_letter = chr(65 + item.correct)
            print(f"Incorrect. The correct answer is {correct_letter}. {item.choices[item.correct]}\n")
            
        quiz_history.append({
            "question": item.prompt,
            "choices": item.choices,
            "answer": user_answer,
            "correct_choice": f"{correct_letter}. {item.choices[item.correct]}" 
        })
        
    print("--------------------")
    print(f"Congratulations! You have scored {score} out of 5 questions")
    
# Saving user's results in a file
        
run_prequiz(sample_ques)
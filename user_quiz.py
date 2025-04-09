# Main Quiz Logic (for user-made quiz)

# import libraries

# class for quiz questions
class UseQuestions:
    def __init__(self, prompt, choices, correct):
        self.prompt = prompt
        self.choices = choices
        self.correct = correct



# function for letting the user add questions
def input_user_quiz():
    user_question = []
    choices_list = []
    
    for number in range(1, 11):
        questions = input(f"\nEnter Question {number}: ")
        user_question.append(questions)
        
        for letter in range(4):
            choices = input(f"  Enter Choice {chr(65 + letter)}: ")
            choices_list.append(choices)

    correct_choice = input(f"What is the correct answer for this question (A/B/C/D)? ").upper()
            
input_user_quiz()
        
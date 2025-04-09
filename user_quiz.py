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
    correct_ans = []
    choices_choose = "ABCD"
    
    for number in range(1, 11):
        print("\n--------------------")
        questions = input(f"\nEnter Question {number}: ")
        user_question.append(questions)
        
        for letter in range(4):
            choices = input(f"  Enter Choice {chr(65 + letter)}: ")
            choices_list.append(choices)
            
        while True:
            correct_choice = input(f"\nWhat is the correct answer for this question? ").upper()
            if correct_choice not in choices_choose:
                print(f"'{correct_choice}' is invalid. Only choose between A, B, C, and D.")
            else:
                correct_ans.append(correct_choice)
                break

            
input_user_quiz()
        
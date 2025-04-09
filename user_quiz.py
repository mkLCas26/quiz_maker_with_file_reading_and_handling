# Main Quiz Logic (for user-made quiz)

# import libraries

# class for quiz questions
class UseQuestions:
    def __init__(self, prompt, choices, correct):
        self.prompt = prompt
        self.choices = choices
        self.correct = correct

user_question = []

# function for letting the user add questions
def input_user_quiz():
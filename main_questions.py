# Main Quiz Logic

# class for quiz questions
class QuizQuestions:
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
    "What is the second most abundant element in the Earth's atmosphere?"
]

# list of questions with choices and correct answer index
quiz_ques = [
    QuizQuestions(
        question_prompts[0],
        ["Pacific Ocean", "Indian Ocean", "Arctic Ocean", "Atlantic Ocean"],
        0
    ),
    
    QuizQuestions(
        question_prompts[1],
        ["Kermadec Trench", "Tonga Trench", "Marianas Trench", "New Britain Trench"],
        2
    ),
    
    QuizQuestions(
        question_prompts[2],
        ["Saturn", "Neptune", "Uranus", "Jupiter"],
        3
    ),
    
    QuizQuestions(
        question_prompts[3],
        ["70%", "71%", "68%", "73%"],
        1
    ),
    
    QuizQuestions(
        question_prompts[4],
        ["Nitrogen", "Argon", "Carbon Dioxide", "Oxygen"],
        3
    )
]
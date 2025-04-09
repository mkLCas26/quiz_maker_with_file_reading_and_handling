# Main Quiz Logic

class QuizQuestions:
    def __init__(self, prompt, choices, correct):
        self.prompt = prompt
        self.choices = choices
        self.correct = correct

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
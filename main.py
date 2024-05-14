from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface

# Creates an empty list
question_bank = []

# Iterates through the response data stored in the data.py retrieved from the API
# Takes out only the question and correct_answer keys and assigns them to variables.
# Passes the variables as a new question object using the Question class
# Appends to the question list to be used in the game as specific question_data
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Quizz logic and functionality are initialized with QuizBrain passing in the question list
quiz = QuizBrain(question_bank)

# Quiz UI is initialized passing in the quizz functionality data type
quizz_ui = QuizzInterface(quiz)

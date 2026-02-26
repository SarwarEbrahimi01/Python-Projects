# Part 2: Write a for loop to iterate ove the question_data.
# Create a Question object from each entry in question_data.
# Append each Question object to the question_bank

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
quiz = QuizBrain(question_bank)
# looping through each question until the questins finished
while quiz.still_has_questions( ):
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
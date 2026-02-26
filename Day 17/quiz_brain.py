# Part 3:

# TODO-1: Asking the questions.
# TODO-2: Checking if the answer was correct.
# TODO-1: Checking if we're the end fo the quiz.
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # Part 4:
    def still_has_questions(self):
        # looping through each question until the questins finished
        # length = len(self.question_list)
        # while self.question_number in range(length):
        #     return True
        # return False
        return self.question_number < len(self.question_list)

    def next_question(self):
        # while self.still_has_questions(): ----> Alternative:looping through each question until the questins finished
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")



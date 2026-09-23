class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def questions_remain(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        return user_answer == correct_answer.lower()

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False): ").lower()

        if self.check_answer(user_answer, current_question.answer.lower()):
            self.score += 1
            print("You got it right!")
        else:
            print(f"That's wrong. The answer was: {current_question.answer}")

        self.question_number += 1
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def tally_score(self):
        if self.score == 12:
            print("Perfect Score! Congratulations!")
        elif self.score >= 8:
            print("Good job!")
        elif self.score >= 4:
            print("Nice try.")
        else:
            print("Oof...")
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def next_question(self):
        current_q = self.questions_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_q.text} (True/False): ")
        self.check_answer(user_input, current_q.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("Correct answer!")
        else:
            print("Wrong answer!")
        print(f"The answer was: {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")
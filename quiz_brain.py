class QuizBrain :
   def __init__(self,q_list) :
      self.question_number = 0
      self.question_list= q_list
      self.score = 0

   @property
   def still_has_question(self) :
      if self.question_number < len(self.question_list):
         return True
      else:
         print("You've completed the quiz!")
         print(f"Score: {self.score}/{self.question_number}")

   def next_question(self):
      current_question = self.question_list[self.question_number]
      user_answer = input(f"Q{self.question_number + 1}: {current_question.text} (True/False): ")
      self.question_number += 1
      self.check_answer(user_answer,current_question.answer)
   def check_answer(self, user_answer, correct_answer) :
      if user_answer.lower() == correct_answer.lower():
         self.score += 1
         print("Correct!")
      else:
         print("Incorrect!")
      print(f"Doğru cevap: {correct_answer}")
      print(f"Score: {self.score}/{self.question_number}")
      print("\n")



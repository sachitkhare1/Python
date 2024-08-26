class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class game:
    def __init__(self, ques):
        self.ques = ques
        self.score = 0

    def play(self):
        for question in self.ques:
            print(question.question)
            for i, option in enumerate(question.options, start=1):
                print(i, option)
            user_choice = input("Enter the number of your answer: ")
            try:
              user_choice = int(user_choice)
              if 1 <= user_choice :
                    if question.check_answer(user_choice):
                        print("Correct!\n")
                        self.score += 1
                    else:
                        print("Incorrect!\n")
              else:
                    print("Invalid choice. Please choose a valid option.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        print("completed =  Your score: ",{self.score} ,len(self.ques))

ques = [
    Question("what is the result of 4*4?", ["44", "16", "42", "87"], 2),
    Question("what is the result of 42/2 ?",["23","34","43","21"], 4),
    Question("what is the result of 5-5?",["0","23","10" ,"55"] , 1),
    Question("What is the result of 3 + 5?", ["7", "8", "9", "10"], 2),
    Question("what is the result of 10+20?", ["32","54","30","20"], 3),
    Question("What is the result of 111+2", ["233", "378", "113", "9854"], 3),
    Question("What is the result of 34*0 ?", ["34" ,"48" ,"12" ,"0"], 4),
    Question("what is the result of 76+24 ?", ["87" , "100" ,"43","438"], 2),
    Question("what is the result of 11+33",["43","223","42","44"] ,4),
    Question("What is the result of 2 * 3?", ["5", "6", "7", "8"], 2)
]

q = game(ques)
q.play() 

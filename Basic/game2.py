
quiz = {
   1 : {"question" : "What is the first name of Iron Man?","answer" : "Tony"},
   2 : {"question" : "Who is called the god of lightning in Avengers?","answer" : "Thor"},
   3 : {"question" : "Who carries a shield of American flag theme in Avengers?","answer" : "Captain America"},
   4 : {"question" : "Which avenger is green in color?","answer" : "Hulk"},
   5 : {"question" : "Which avenger can change it's size?","answer" : "AntMan"},
   6 : {"question" : "Which Avenger is red in color and has mind stone?","answer" : "Vision"}}

def check_ans(question, ans, attempts, score):
    if quiz[question]['answer'].lower() == ans.lower():
        print("Correct Answer. \n Your score is :",{score + 1})
        return True
   
def play():
   score =0
   for ques in quiz:
    attempts = 3 
    while attempts > 0: 
        print(quiz[ques]['question']) 
        answer = input("Enter Answer: ")
        check = check_ans(ques, answer, attempts, score)
        if check:
            score += 1
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Wrong Answer :( You have, ",{attempts} ,"attempts left. Try again...")
            else:
                print("Out of attempts The correct answer was:", {quiz[ques]['answer']})
                exit()
    
play()
   
# quiz = {
#     1: {"question": "What is the result of 4*4?", "answer": "16"},
#     2: {"question": "What is the result of 42/2?", "answer": "21"},
#     3: {"question": "What is the result of 5-5?", "answer": "0"},
#     4: {"question": "What is the result of 3 + 5?", "answer": "8"},
#     5: {"question": "What is the result of 10+20?", "answer": "30"},
#     6: {"question": "What is the result of 111+2?", "answer": "113"},
#     7: {"question": "What is the result of 34*0?", "answer": "0"},
#     8: {"question": "What is the result of 76+24?", "answer": "100"},
#     9: {"question": "What is the result of 11+33?", "answer": "44"},
#     10: {"question": "What is the result of 2 * 3?", "answer": "6"}
# }

# def check_ans(question, ans):
#     return quiz[question]['answer'] == ans

# def play():
#     score = 0
#     for question_id in quiz:
#         attempts = 3
#         while attempts > 0:
#             print(quiz[question_id]['question'])
#             answer = input("Enter Answer: ")
#             if check_ans(question_id, answer):
#                 score += 1
#                 print("Correct Answer! Your score is:" ,{score})
#                 break
#             else:
#                 attempts -= 1
#                 if attempts > 0:
#                     print("Wrong Answer :( You have, ",{attempts} ,"attempts left. Try again...")
#                 else:
#                     print("Out of attempts! The correct answer was:", {quiz[question_id]['answer']})
#                     exit()
#         print()
#     print("quiz finished Your final score is:", {score})

# play()

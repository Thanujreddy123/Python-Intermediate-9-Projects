from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain

question_bank=[]
for i in question_data:
    question_bank.append(Question(i['text'],i['answer']))

quiz=Quiz_brain(question_bank)
while quiz.still_has_question():
    quiz.next_question();
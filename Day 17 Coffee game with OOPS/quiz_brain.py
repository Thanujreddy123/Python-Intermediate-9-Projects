class Quiz_brain:
    def __init__(self,questionlist):
        self.questionnumber=0
        self.score=0
        self.question_list=questionlist

    def checkanswer(self,useranswer,result):
        if useranswer.lower()==result.lower():
            self.score=self.score+1
            print("you got it right you got one point")
        else:
            print("you got wrong answer")
        print(self.score,"your score")
    def next_question(self):
        current_question=self.question_list[self.questionnumber]
        self.questionnumber  +=1
        result=input(f"{self.questionnumber},{current_question.text} guess answer")
        self.checkanswer(result,current_question.answer)

    def still_has_question(self):
        return self.questionnumber<len(self.question_list)
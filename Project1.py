import re

class SimpleQuiz():
    
    def __init__(self):
        self.questions = {1:"What is the largest internal organ in the human body?\n",2:"What percentage of the Earth’s surface is covered by water?\n",3:"What is the atomic number of Hydrogen?\n"}
        self.options = {1:["A) Lungs\t","B) Heart\t","C) Kidneys\t","D) Liver\n"] ,2:["A) 51%\t","B) 61%\t","C) 71%\t","D) 81%\n"] ,3:["A) 1\t","B) 2\t","C) 3\t","D) 4\n"]}        
        self.answers = {1:'D' ,2:'C' ,3:'A'}
        self.char_to_no = {'A':0,'B':1,'C':2,'D':3}
        self.score = 0
        self.option_validator = r'[ABCD]$'
        self.choice_validator = r'[yn]'
        self.number_validator = r'[1-4]'
        print("Welcome in a simple Quiz\nEach question posses 10 Marks\n")
        self.showMenu()

    def showMenu(self):
        print("Welcome in a simple Quiz Game\n")
        ch = input("1.play game\n2.Customize Quiz\n Press any key to exit\n")
        if ch =='1':
            self.startQuiz()
        elif ch =='2':
            self.customizeQuizMenu()
        else:
            pass
    
    def customizeQuizMenu(self):
        print("customize:\n1.Questions\n2.Options\n3.Answers\nPress any key to exit\n")
        ch = input("write your option here:\t")

        if ch == '1':
            self.customizeQuiz(1)
        elif ch == '2':
            self.customizeQuiz(2)
        elif ch == '3':
            self.customizeQuiz(3)
        else:
            self.showMenu()

    def showQuestions(self):
        for i in range(len(self.questions)):
            print("\nquestion ",i+1,":\n"+self.questions.get(i+1)+"\n"+"".join(self.options.get(i+1))+"\nAnswer:\t"+self.answers.get(i+1))
            
    def customizeQuiz(self,choice):
        if choice == 1:
            print("\n1.Add new questions to existing Questions\n2.Update question in existing question\nPress any key to exit\n")
            ch = input("your choice :\t")
            if ch == '1':
                counter = 1
                while(counter):
                    counter2 = 1
                    ques = input("Enter your question:\n")
                    optionA = input("Enter option A:\t")
                    optionB = input("Enter option B:\t")
                    optionC = input("Enter option C:\t")
                    optionD = input("Enter option D:\t")
                    answer = input("\nEnter answer:\t").capitalize()
                    self.questions[len(self.questions)+1] = ques
                    self.options[len(self.options)+1] = ["A)"+optionA+"\t","B)"+optionB+"\t","C)"+optionC+"\t","D)"+optionD]
                    self.answers[len(self.answers)+1] = answer
                    print("New Question is added successfully")
                    while(counter2):
                        c = input("Add Another Question? Y/N:\t").lower()
                        if re.search(self.choice_validator,c):
                            print(c)
                            if c == 'y':
                                counter = 1
                                counter2 = 0
                            else:
                                self.showQuestions()
                                self.customizeQuiz(1)
                                counter = 0
                        else:
                            print("Please use options keywords --> Y/N")
                            counter2 = 1
                    
            
            elif ch == '2':
                counter = 1
                while(counter):
                    print("these are the existing question you can change")
                    self.showQuestions()
                    ques_no = int(input("what question no. do you want to customize?:\t"))
                    ques = input("Write the updated question\n")
                    self.questions[ques_no] = ques
                    print("Question is updated succefully")
                    c = input("Add Another Question? Y/N:\t").lower()
                    if c == 'y':
                        counter = 1
                        
                    else:
                        self.showQuestions()
                        self.customizeQuiz(1)
                        counter = 0
                
            else:
                self.customizeQuizMenu()
        elif choice == 2:
            self.showQuestions()
            counter = 1
            while(counter):
                ques_no = input("Enter the Question no. of which you want to change the option:\t")
                if re.search(self.number_validator,ques_no):
                    counter = 0
                else:
                    print("Please use this keyword ---> 1,2,3,4")
            counter = 1
            while(counter):
                option = input("Enter the option alphabate you want to change:\t").capitalize()
                if re.search(self.option_validator,option):
                    option_no = self.char_to_no[option]
                    counter = 0
                else:
                    print("Please use this keyword ---> A,B,C,D")
            
            option = option+")" + input("Enter your new option here:\t")+"\t"
            self.options[int(ques_no)][option_no] = option
            print(ques_no, option_no,option)
            print("Option is added successfully")
            self.showQuestions()
            pass
        elif choice == 3:
            self.showQuestions()
            counter = 1
            while(counter):
                ques_no = input("Enter the Question no. of which you want to change the option:\t")
                if re.search(self.number_validator,ques_no):
                    counter = 0
                else:
                    print("Please use this keyword ---> 1,2,3,4")
            counter = 1
            while(counter):
                answer = input("Enter the correct option here:\t").capitalize()
                if re.search(self.option_validator,answer):
                    counter = 0
                else:
                    print("Please use this keyword ---> A,B,C,D")
            self.answers[ques_no] = answer
            print("Correct answer is updated successfully!!")

    def startQuiz(self):
        ch = 'y'
        i = 1
        answer = ''
        print("Each question posses 10 Marks\n")
        for q in range(len(self.questions)) :
            counter = 1 #for finding if user had type the only applicable key
            print("\n",self.questions.get(q+1),"\n","".join(self.options.get(q+1)))
            while(counter):
                answer = input("Answer:\t").capitalize()

                if re.search(self.option_validator,answer):
                    if self.answers[i] == answer:
                        print("your answer is correct\n")
                        self.score = self.score+10

                    else:
                        print("you are wrong, right answer is:\t",self.answers[i])
                    i = i+1
                    counter = 0

                else:
                    print("Please use options keywords --> a,b,c,d")
                    
        print("Your final score is: ",self.score,"\n")
        counter = 1
        while(counter):
            ch = input("Want to play again? Y/N:\t").lower()
            if re.search(self.choice_validator,ch):
                if ch == 'y':
                    self.score = 0
                    self.startQuiz()
                else:
                    self.showMenu()
                counter = 0
            else:
                print("Please use options keywords --> Y/N")
                counter = 1

if __name__ == '__main__':
    s = SimpleQuiz()